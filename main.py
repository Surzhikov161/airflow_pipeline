from airflow import DAG
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from src.python_jobs.add_to_gp import get_queries


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
    "astondevs_airflow_gp_practice",
    default_args=default_args,
    description="test dag",
    schedule_interval=timedelta(days=1),
    catchup=False,
    max_active_runs=1,
)


def create_gp_task(query, task_id, dag):
    def gp_task():
        execute_sql(query)
        print(f"SUCCESS: {task_id}")

    return PythonOperator(
        task_id=task_id,
        python_callable=gp_task,
        dag=dag,
    )


info_for_tasks = [(query, task_id) for query, task_id in get_queries()]

gp_tasks = []
for query, task_id in info_for_tasks:
    task = create_gp_task(query, task_id, main_dag)
    gp_tasks.append(task)

gp_tasks
