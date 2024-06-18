import org.apache.hadoop.conf.Configuration
import org.apache.hadoop.fs.{FileSystem, Path,LocatedFileStatus, RemoteIterator}
import org.apache.spark.sql.DataFrame
import java.net.URI
import org.apache.spark.sql.SparkSession
import java.io.{File, FileOutputStream}
import java.sql.{Connection, DriverManager}
import java.sql.Statement


object Main extends App {

  
  val spark = SparkSession.builder
    .appName("pxf_job")
    .master("local[8]")
    .config("spark.master", "local")
    .getOrCreate()

  val url = "jdbc:postgresql://172.17.1.32:5432/postgres"
  val username = "wave2_user_a2"
  val password = "pass"

  val connection: Connection = DriverManager.getConnection(url, username, password)
  val statement: Statement = connection.createStatement()
  
  val uriToHDFS = new URI("hdfs://172.17.0.23:8020/user/a.surzhikov/")
  // тестовый zipfile
  val dirName = "parsed_gar"
  val pathToFile = s"${uriToHDFS.toString}$dirName"
  
  val hdfs: FileSystem = FileSystem.get(uriToHDFS, new Configuration())
  val files: RemoteIterator[LocatedFileStatus] = hdfs.listFiles(new org.apache.hadoop.fs.Path(pathToFile), true)
  while (files.hasNext) {
    val file: LocatedFileStatus = files.next()
    val path = file.getPath().getParent().toString
    val df = spark.read.parquet(path)
    df.dtypes
  }  
  
  spark.stop()
}