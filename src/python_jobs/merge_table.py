from src.utils import execute_sql


def merge_table():
    query = "CALL public.surzhiko_procedure('public.surzhikov_pxf_as_addhouse_types', 'public.surzhikov_pxf_as_house_types')"
    execute_sql(query)
