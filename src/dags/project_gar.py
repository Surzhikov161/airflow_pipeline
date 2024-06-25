from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import (
    SparkSubmitOperator,
)
import os
from src.python_jobs_for_aston.data_generator import generator_map
from src.python_jobs_for_aston.hdsf_stg import add_to_hdfs
from src.config.config import aston_filenames, hdfs_path_to_my_dir, data_dir

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 1, 1),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


main_dag = DAG(
    "asurzhikov_aston_project_dag",
    default_args=default_args,
    description="test dag",
    schedule_interval=timedelta(days=1),
    catchup=False,
    max_active_runs=1,
)


def create_task_for_generate(fileName: str, func):
    return PythonOperator(
        task_id=f"generate_{fileName}",
        python_callable=func,
        dag=main_dag,
    )


generate_tasks = []

for fileName, func in generator_map.items():
    generate_tasks.append(create_task_for_generate(fileName, func))


def create_stg_task(path: str):
    tmp_path = path.replace("/", "_")[:-4]
    task_id = f"put_to_stg_{tmp_path}"
    return PythonOperator(
        task_id=task_id,
        python_callable=add_to_hdfs,
        op_args=[path],
        dag=main_dag,
    )


def create_hdfs_dds_task(path: str):
    tmp_path = path.replace("/", "_")[:-4]
    task_id = f"{tmp_path}_to_parquet"
    return SparkSubmitOperator(
        application="src/python_jobs_for_aston/hdfs_dds.py",  # путь к PySpark скрипту
        task_id=task_id,
        conn_id="spark_default",
        application_args=[path],
        dag=main_dag,
    )


stg_tasks = []
dds_tasks = []
for name in aston_filenames:
    path = os.path.join(data_dir, name + ".csv")
    stg_tasks.append(create_stg_task(path))
    dds_tasks.append(create_hdfs_dds_task(path))


def create_hive_task(uri, name):
    task_id = f"create_hive_table_{name}"
    return SparkSubmitOperator(
        application="src/python_jobs_for_aston/create_hive_tables.py",  # путь к PySpark скрипту
        task_id=task_id,
        conn_id="spark_default",
        application_args=[uri + name, name],
        dag=main_dag,
    )


def create_clean_task(uri, name):
    task_id = f"clean_data_in_{name}"
    return SparkSubmitOperator(
        application="src/python_jobs_for_aston/data_cleaning.py",  # путь к PySpark скрипту
        task_id=task_id,
        conn_id="spark_default",
        application_args=[uri + name, name],
        dag=main_dag,
    )


info_for_hive_task = zip([f"{hdfs_path_to_my_dir}/dds/"] * 4, aston_filenames)
hive_tasks = []
cleaning_tasks = []
for uri, name in info_for_hive_task:
    hive_tasks.append(create_hive_task(uri, name))
    cleaning_tasks.append(create_clean_task(uri, name))

generate_tasks
for gen_task in generate_tasks:
    for stg_task in stg_tasks:
        gen_task >> stg_task
for stg_task in stg_tasks:
    for dds_task in dds_tasks:
        stg_task >> dds_task
for dds_task in dds_tasks:
    for hive_task in hive_tasks:
        dds_task >> hive_task
for hive_task in hive_tasks:
    for clean_task in cleaning_tasks:
        hive_task >> clean_task
