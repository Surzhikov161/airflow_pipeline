import sys
from zipfile import PyZipFile

zip_file = sys.argv[1]
path = sys.argv[2]

pzf = PyZipFile(zip_file)
pzf.extractall(path)

# hadoop fs -copyToLocal <hdfs_input_file_path> <output_path> | python3 unzip.py <output_path> <unzipped_output> | hadoop fs -put <unzipped_output> <hdfs_path>
