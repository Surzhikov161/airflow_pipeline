from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import sys
from src.config.config import hdfs_path_to_my_dir

try:
    file_path = sys.argv[1]
    name = sys.argv[2]
except:
    sys.exit(1)

spark = (
    SparkSession.builder.appName("STG GreenPlum")
    .master("local[*]")
    .getOrCreate()
)

df = spark.read.parquet(file_path)
resDf = df.dropDuplicates().dropna()

resDf.write.format("jdbc").options(
    url="jdbc:postgresql://172.17.1.32:5432/postgres",
    dbtable=f"stg.asurzhikov_{name}",
    user="wave2_user_a2",
    password="pass",
    driver="org.postgresql.Driver",
).mode("overwrite").save()
