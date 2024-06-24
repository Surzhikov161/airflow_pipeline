import pyarrow.fs
import os
import re
from zipfile import PyZipFile
from pyspark.sql import SparkSession
import xml.etree.ElementTree as ET
from src.config.config import (
    hdfs_uri,
    hdfs_user,
    zipname,
    unzip_path,
    parsed_path,
    unzip_dir,
    my_dir,
    hdfs_port,
)
from functools import reduce


class ParseZip:
    path_to_zip = f"{my_dir}/{zipname}"

    def __init__(self, hdfs_uri: str, user: str):
        self.hdfs = pyarrow.fs.HadoopFileSystem(hdfs_uri, user=hdfs_user)
        self.spark = (
            SparkSession.builder.appName("Parse xml into parquet").master(
                "local[*]"
            )
            # .config("spark.jars", "spark-xml_2.12-0.18.0.jar")
            # .config("spark.executor.extraClassPath", "spark-xml_2.12-0.18.0.jar")
            # .config("spark.executor.extraLibrary", "spark-xml_2.12-0.18.0.jar")
            # .config("spark.driver.extraClassPath", "spark-xml_2.12-0.18.0.jar")
            .getOrCreate()
        )

    def get_file(self):
        return self.hdfs.open_input_file(self.path_to_zip)

    def unzip(self):
        pzf = PyZipFile(self.get_file())
        zipinfos = pzf.infolist()
        for zipinfo in zipinfos:
            zipinfo.filename = re.sub(
                r"_[0-9].+\.", ".", zipinfo.filename
            ).lower()
            pzf.extract(zipinfo, unzip_path)

    def parse_xmls(self):
        for fpath, _, files in os.walk(unzip_path):

            for file_name in files:
                print(f"======== Parsing {file_name} ======== ")
                save_path = os.path.join(
                    fpath.replace(unzip_dir, parsed_path), file_name[:-4]
                )
                path = os.path.join(fpath, file_name)
                if file_name.endswith(".txt"):
                    df = self.spark.read.text(path)
                    # df.write.mode("overwrite").parquet(save_path)
                    print(f"======== Saving {file_name} to HDFS ======== ")
                    df.write.mode("overwrite").parquet(
                        f"{hdfs_uri}:{hdfs_port}/user/{hdfs_user}/{save_path}"
                    )
                    print(f"======== Success save of {file_name} ======== \n")
                elif file_name.endswith(".xml"):
                    tree = ET.parse(path)
                    root = tree.getroot()
                    rowTag = root[0].tag
                    sourceDf = (
                        self.spark.read.format("com.databricks.spark.xml")
                        .option("rowTag", rowTag)
                        .load(path)
                    )
                    resDf = reduce(
                        lambda acc, col: acc.withColumnRenamed(
                            col, col.lower()
                        ),
                        sourceDf.columns,
                        sourceDf,
                    )
                    # resDf.write.mode("overwrite").parquet(save_path)
                    print(f"======== Saving {file_name} to HDFS ======== ")
                    resDf.write.mode("overwrite").parquet(
                        f"{hdfs_uri}:{hdfs_port}/user/{hdfs_user}/{save_path}"
                    )
                    print(f"======== Success save of {file_name} ======== \n")
                else:
                    print(f"======== Unexpected file type ======== \n")
        print("======== Parsing end without errors ========")


def run_parse():
    parser = ParseZip(hdfs_uri, hdfs_user)
    parser.unzip()
    parser.parse_xmls()


run_parse()
