import pyarrow.fs

from src.config.config import (
    hdfs_uri,
    hdfs_user,
    hdfs_uri,
    zipname,
    zip_save_path,
)


def add_to_hdfs():
    pyarrow.fs.copy_files(zipname, zip_save_path)
