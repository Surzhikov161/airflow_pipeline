from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import (
    SparkSubmitOperator,
)
from src.python_jobs_for_gar.merge_table import merge_table
from src.python_jobs_for_gar.add_zip_to_hdfs import add_to_hdfs


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
    "asurzhikov_dag",
    default_args=default_args,
    description="test dag",
    schedule_interval=timedelta(days=1),
    catchup=False,
    max_active_runs=1,
)


put_to_hdfs = PythonOperator(
    task_id="put_to_hdfs", python_callable=add_to_hdfs
)


parse_zip = SparkSubmitOperator(
    application="src/python_jobs_for_gar/parse_zip.py",  # путь к PySpark скрипту
    task_id="spark_parse_zip",
    conn_id="spark_default",
    dag=main_dag,
)


add_to_gp = SparkSubmitOperator(
    application="src/python_jobs_for_gar/add_to_gp.py",  # путь к PySpark скрипту
    task_id="add_to_gp",
    conn_id="spark_default",
    dag=main_dag,
)

create_merge_table = PythonOperator(
    task_id="create_merge_table", python_callable=merge_table
)

put_to_hdfs >> parse_zip >> add_to_gp >> create_merge_table
