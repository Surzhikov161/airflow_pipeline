from dotenv import load_dotenv, find_dotenv
import os
import re

# export CLASSPATH=`../../hadoop/bin/hdfs classpath --glob`
if not find_dotenv():
    exit("ERROR: Not found .env file")
else:
    # os.environ["ARROW_LIBHDFS_DIR"] = "../../hadoop/lib/native/"
    load_dotenv()

unzip_dir = os.environ.get("UNZIP_PATH")
parsed_path = os.environ.get("PARSED_PATH")
zipname = os.environ.get("ZIP_NAME")
hdfs_uri = os.environ.get("HDFS_URI")
hdfs_user = os.environ.get("HDFS_USER")
hdfs_port = os.environ.get("HDFS_PORT")
unzip_path = os.path.join(unzip_dir, re.sub(r"\..+", "", zipname))
my_dir = f"/user/{hdfs_user}"
hdfs_path_to_my_dir = f"{hdfs_uri}:{hdfs_port}{my_dir}"
zip_save_path = f"{hdfs_path_to_my_dir}/{zipname}"
stg_path = f"{hdfs_path_to_my_dir}/stg"
os.environ["HADOOP_USER_NAME"] = hdfs_user
os.environ["ARROW_LIBHDFS_DIR"] = "../hadoop/lib/native/"

aston_filenames = [
    "bank_transactions",
    "clients",
    "securities",
    "security_transactions",
]
