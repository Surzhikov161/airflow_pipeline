from pyspark.sql import SparkSession
import sys

try:
    file_path = sys.argv[1]
    name = sys.argv[2]
except:
    sys.exit(1)

spark = (
    SparkSession.builder.appName("hive tables")
    .master("local[*]")
    .getOrCreate()
)

df = spark.read.parquet(file_path)
df.write.mode("overwrite").saveAsTable(f"asurzhikov.{name}")
