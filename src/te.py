from datetime import datetime, timedelta
from airflow import DAG
from sqlalchemy import create_engine
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook


public_schema = "public"
raw_schema = "raw"
stg_shema = "stg"
dds_shema = "dds"
dm_shema = "dm"


transactions_table_name = "transactions"
clients_table_name = "clients"
currency_table_name = "currency_rate"
temp_suffix = "_temp"


# Определяем простую функцию, которая будет выполняться в задаче
def print_hello():
    print("Hello, Airflow!")
    print("Hello, 23.05.2024!")
    print("Hello, 29.05.2024!")


def execute_sql(query):
    # Получение подключения из Airflow
    hook = PostgresHook(postgres_conn_id="gp_default")
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


def moex_extract_data():
    # Загрузка данных из CSV файла
    file_path = "/opt/airflow/upload/af_gp/moex.csv"
    data_source = pd.read_csv(file_path, delimiter=";")
    data = pd.DataFrame.from_dict(data_source)
    print("data.count: ", data.iloc[0])
    return data


def load_data(file_path, schema, table):
    # Чтение CSV-файла
    data_source = pd.read_csv(file_path, delimiter=";")
    data = pd.DataFrame.from_dict(data_source)

    # Получение подключения из Airflow
    hook = PostgresHook(postgres_conn_id="gp_default")
    conn_string = hook.get_uri().replace("__extra__=", "")
    temp_table = f"{table}{temp_suffix}"

    # Подключение к базе данных Greenplum с использованием SQLAlchemy
    engine = create_engine(conn_string)

    with engine.connect() as connection:
        # Создание временной таблицы
        data.head(0).to_sql(
            temp_table,
            connection,
            schema=schema,
            if_exists="replace",
            index=False,
        )

        # Загрузка данных во временную таблицу
        data.to_sql(
            temp_table,
            connection,
            schema=schema,
            if_exists="append",
            index=False,
        )

        # Перемещение данных из временной таблицы в целевую таблицу
        connection.execute(
            f"""
        BEGIN;
        DROP TABLE IF EXISTS {schema}.{table};
        ALTER TABLE {schema}.{temp_table} RENAME TO {table};
        COMMIT;
        """
        )

    print(f"Data loaded successfully into {schema}.{table}.")


# def moex_load_data(**kwargs):
#     load_data('/opt/airflow/upload/af_gp/moex.csv', public_schema,transactions_table_name)
#     print("SUCCESS: moex_load_data")


def create_load_data_task(file_path, schema_name, table_name, task_id, dag):
    def load_data_task():
        load_data(file_path, schema_name, table_name)
        print(f"SUCCESS: {task_id}")

    return PythonOperator(
        task_id=task_id,
        python_callable=load_data_task,
        dag=dag,
    )


# Определяем DAG
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 1, 1),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "astondevs_airflow_gp_practice",
    default_args=default_args,
    description="A simple hello world DAG",
    schedule_interval=timedelta(days=1),
    catchup=False,
    max_active_runs=1,
)

# Определяем тестовую задачу
hello_task = PythonOperator(
    task_id="hello_task",
    python_callable=print_hello,
    dag=dag,
)

#
# Демонстрация динамического формирования тасок с параллельным запуском
#

# Определение файлов и соответствующих таблиц
files_and_tables = [
    ("/opt/airflow/upload/af_gp/clients.csv", raw_schema, clients_table_name),
    (
        "/opt/airflow/upload/af_gp/currency_rate.csv",
        raw_schema,
        currency_table_name,
    ),
    (
        "/opt/airflow/upload/af_gp/transactions.csv",
        raw_schema,
        transactions_table_name,
    ),
]

# Создание задач динамически
load_data_tasks = []
for file_path, schema_name, table_name in files_and_tables:
    task_id = f"load_data_task_{table_name}"
    task = create_load_data_task(
        file_path, schema_name, table_name, task_id, dag
    )
    load_data_tasks.append(task)


#
# Демонстрация динамического формирования тасок с последовательным запуском
#

# Список процедур для вызова
procedures = [
    "CALL dds.transform_and_load_clients();",
    "CALL dds.transform_and_load_currency_rate();",
    "CALL dds.transform_and_load_transactions();",
]

# Создание задач execute_sql_tasks динамически
execute_sql_tasks = []
for i, procedure in enumerate(procedures):
    task_id = f"execute_task_{i+1}"
    task = PythonOperator(
        task_id=task_id,
        python_callable=lambda p=procedure: execute_sql(p),
        dag=dag,
    )
    execute_sql_tasks.append(task)

# Установка зависимостей между задачами
hello_task >> load_data_tasks
for load_task in load_data_tasks:
    for exec_task in execute_sql_tasks:
        load_task >> exec_task
