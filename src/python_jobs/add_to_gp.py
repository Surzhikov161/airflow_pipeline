import os
import pyarrow.fs
from pyspark.sql import SparkSession
from airflow.providers.postgres.hooks.postgres import PostgresHook

from src.config.config import (
    hdfs_uri,
    hdfs_user,
    my_dir,
    parsed_path,
    hdfs_uri,
    hdfs_port,
)

public_schema = "public"


spark = (
    SparkSession.builder.appName("Make pxf table in gp").master("local[*]")
    # .config("spark.jars", "spark-xml_2.12-0.18.0.jar")
    # .config("spark.executor.extraClassPath", "spark-xml_2.12-0.18.0.jar")
    # .config("spark.executor.extraLibrary", "spark-xml_2.12-0.18.0.jar")
    # .config("spark.driver.extraClassPath", "spark-xml_2.12-0.18.0.jar")
    .getOrCreate()
)

hdfs = pyarrow.fs.HadoopFileSystem(hdfs_uri, user=hdfs_user)

pathToParquet = f"{my_dir}/{parsed_path}"

all_files = hdfs.get_file_info(
    pyarrow.fs.FileSelector(pathToParquet, recursive=True)
)
dir_name = "scripts"
os.mkdir(dir_name)
for fileInfo in all_files:
    if not fileInfo.is_file and "as_" in fileInfo.path.lower():
        tmp_name = fileInfo.path.replace("/", "_")
        script_path = os.path.join(dir_name, f"script_for_gp_{tmp_name}.sql")
        with open(script_path, "w") as f:
            df = spark.read.parquet(f"{hdfs_uri}:{hdfs_port}{fileInfo.path}")
            df_types = df.dtypes

            query = f"""
                CREATE EXTERNAL TABLE {public_schema}.surzhikov_pxf_{fileInfo.base_name} (
                    {", ".join([f"{col} {dtype}" for col, dtype in df_types])}
                    )
                LOCATION ('pxf:/{fileInfo.path}?PROFILE=hdfs:parquet')
                FORMAT 'CUSTOM' (FORMATTER='pxfwritable_import');
                """
            f.write(query + "\n")
