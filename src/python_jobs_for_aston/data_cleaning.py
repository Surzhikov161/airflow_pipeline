from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import sys
from src.config.config import gp_user, gp_uri, gp_pass

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
    url=gp_uri,
    dbtable=f"stg.asurzhikov_{name}",
    user=gp_user,
    password=gp_pass,
    driver="org.postgresql.Driver",
).mode("overwrite").save()
