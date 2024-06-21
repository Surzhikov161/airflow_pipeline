import sys
import pyarrow.fs
from pyspark.sql import SparkSession
from src.utils import execute_sql
from src.config.config import (
    hdfs_uri,
    hdfs_user,
    my_dir,
    parsed_path,
    hdfs_uri,
    hdfs_port,
    zipname,
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

pathToParquet = f"{my_dir}/{parsed_path}/{zipname[:-4]}"

all_files = hdfs.get_file_info(
    pyarrow.fs.FileSelector(pathToParquet, recursive=True)
)

for fileInfo in all_files:
    if not fileInfo.is_file and "as_" in fileInfo.path.lower():
        df = spark.read.parquet(f"{hdfs_uri}:{hdfs_port}{fileInfo.path}")
        df_types = df.dtypes

        query = f"""
            CREATE EXTERNAL TABLE {public_schema}.surzhikov_pxf_{fileInfo.base_name} (
                {", ".join([f"{col} {dtype if dtype != 'string' else 'text'}" for col, dtype in df_types])}
                )
            LOCATION ('pxf:/{fileInfo.path}?PROFILE=hdfs:parquet')
            FORMAT 'CUSTOM' (FORMATTER='pxfwritable_import');
            """
        execute_sql(query)
