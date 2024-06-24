import pyarrow.fs

from src.config.config import (
    stg_path,
)


def add_to_hdfs(path: str):
    print(path)
    csv_name = path.split("/")[-1]
    pyarrow.fs.copy_files(path, f"{stg_path}/{csv_name}")
