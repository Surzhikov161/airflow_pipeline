from airflow import DAG
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.providers.apache.spark.operators.spark_submit import (
    SparkSubmitOperator,
)

from src.config.config import zipname, hdfs_user

# from src.python_jobs.parse_zip import run_parse


def execute_sql(query):
    # Получение подключения из Airflow
    hook = PostgresHook(postgres_conn_id="asurzhikov_gp_conn")
    conn = hook.get_conn()
    cursor = conn.cursor()

    # Выполнение SQL-скрипта
    cursor.execute(query)

    # Подтверждение транзакции
    conn.commit()

    # Закрытие соединения
    cursor.close()
    conn.close()

    print("SUCCESS: Executed SQL script")


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
    "asurzhikov_dag_test",
    default_args=default_args,
    description="test dag",
    schedule_interval=timedelta(days=1),
    catchup=False,
    max_active_runs=1,
)

put_to_hdfs = BashOperator(
    task_id="put_to_hdfs",
    depends_on_past=False,
    bash_command=f"hdfs dfs -put -f /opt/airflow/dags/files/{zipname} /user/{hdfs_user}",
    dag=main_dag,
)

# parse_zipfile = PythonOperator(
#     task_id="Parse zipfile",
#     python_callable=run_parse,
#     dag=main_dag,
# )


def create_gp_task(query, task_id, dag):
    def gp_task():
        execute_sql(query)
        print(f"SUCCESS: {task_id}")

    return PythonOperator(
        task_id=task_id,
        python_callable=gp_task,
        dag=dag,
    )


spark_submit_task = SparkSubmitOperator(
    application="python_jobs/add_to_gp.py",  # путь к PySpark скрипту
    task_id="spark_submit_task",
    conn_id="spark_default",
    dag=main_dag,
)

# info_for_tasks = [(query, task_id) for query, task_id in get_queries()]

# gp_tasks = []
# for query, task_id in info_for_tasks:
#     task = create_gp_task(query, task_id, main_dag)
#     gp_tasks.append(task)

spark_submit_task
