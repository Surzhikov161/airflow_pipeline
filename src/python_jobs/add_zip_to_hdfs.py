import pyarrow.fs

from src.config.config import (
    hdfs_uri,
    hdfs_user,
    hdfs_uri,
    zipname,
    save_path,
)


def add_to_hdfs():
    pyarrow.fs.copy_files(zipname, save_path)
