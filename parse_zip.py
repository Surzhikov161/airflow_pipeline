# import sys
# from zipfile import PyZipFile
#
# zip_file = sys.argv[1]
# path = sys.argv[2]
#
# pzf = PyZipFile(zip_file)
# pzf.extractall(path)

import os

import pyarrow.fs

os.environ["ARROW_LIBHDFS_DIR"] = "../hadoop-3.3.6/lib/native/"
os.environ["CLASSPATH"] = "../hadoop-3.3.6/share/hadoop/common/lib"
# Устанавливаем путь к HDFS
hdfs = pyarrow.fs.HadoopFileSystem("hdfs://172.17.0.23:8020")

# Читаем файл из HDFS
# file = hdfs.open_input_file("/path/to/file/in/hdfs")
# data = file.read().to_pybytes()

# Печатаем содержимое файла
# print(data)
