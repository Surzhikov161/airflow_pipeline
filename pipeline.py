from datetime import datetime, timedelta
from airflow import DAG

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 5, 1),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "astondevs_airflow_a.surzhikov_pipeline",
    default_args=default_args,
    description="Pipeline hdfs",
    schedule_interval=timedelta(days=1),
    catchup=False,
    max_active_runs=1,
)
