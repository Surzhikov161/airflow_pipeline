from airflow.providers.postgres.hooks.postgres import PostgresHook


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
