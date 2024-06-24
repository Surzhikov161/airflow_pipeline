from pyspark.sql import SparkSession
import sys
from src.config.config import stg_path, hdfs_path_to_my_dir

try:
    file_path = sys.argv[1]
except:
    sys.exit(1)
# file_path = "data/security_transactions.csv"

spark = (
    SparkSession.builder.appName("stg to dds").master("local[*]").getOrCreate()
)
csv_name = file_path.split("/")[-1]
df = (
    spark.read.option("header", "true")
    .option("inferSchema", "true")
    .csv(f"{stg_path}/{csv_name}")
)

df.write.mode("overwrite").parquet(
    f"{hdfs_path_to_my_dir}/dds/{csv_name[:-4]}"
)
