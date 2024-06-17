import org.apache.hadoop.conf.Configuration
import org.apache.hadoop.fs.{FileSystem, Path}
import org.apache.spark.sql.DataFrame
import java.net.URI
import scala.collection.immutable.Stream
import java.util.zip.{ZipEntry, ZipInputStream}
import org.apache.spark.sql.SparkSession
import java.nio.file.{Paths, Path}
import scala.xml.{XML, Elem}
import java.io.{File, FileOutputStream}


// sys.exit(1)
object Main extends App {

  // val test = {
  //   try {
  //     println(sys.env)
  //     sys.env("ZIPNAME")
  //   } catch {
  //     case e: NoSuchElementException => {
  //       println("====== No envirable ======")
  //       sys.exit(1)
  //     }
  //   }
  // }

  
  val spark = SparkSession.builder
    .appName("Parse ZipFile")
    .master("local[8]")
    .config("spark.master", "local")
    .getOrCreate()


  val uriToHDFS = new URI("hdfs://172.17.0.23:8020/user/a.surzhikov/")
  // тестовый zipfile
  val zipName = "gar_delta_xml.zip"
  val pathToFile = s"${uriToHDFS.toString}$zipName"
  
  val hdfs = FileSystem.get(uriToHDFS, new Configuration())
  val path = new org.apache.hadoop.fs.Path(pathToFile)
  val stream = hdfs.open(path)

  val zis: ZipInputStream = new ZipInputStream(stream)
  
  val unzip_dir: java.nio.file.Path = Paths.get("unzip_gar")
  val outputParsedPath: java.nio.file.Path = Paths.get("parsed_gar")


  Stream.continually(zis.getNextEntry).takeWhile(_ != null).foreach { file: ZipEntry =>
    if (!file.isDirectory) {
      println(s"======= Reading ${file.getName} =======")
      val format = file.getName.substring(file.getName.indexOf("."))
      val fileName = {
        val tmp = file.getName.replaceAll("_[0-9].+", "")
        if (tmp.indexOf(".") == -1){
          tmp + format
        } else {tmp}
        
      }
      val parquetPath: java.nio.file.Path = outputParsedPath.resolve(fileName)
      val outPath: java.nio.file.Path = unzip_dir.resolve(fileName)
      val outPathParent: java.nio.file.Path = outPath.getParent
      
      if (!outPathParent.toFile.exists()) {
        outPathParent.toFile.mkdirs()
      }

      val outFile: File = outPath.toFile
      val out: FileOutputStream = new FileOutputStream(outFile)
      val buffer: Array[Byte] = new Array[Byte](4096)
      
      println(s"======= Unpacking ${file.getName}... =======")
      Stream.continually(zis.read(buffer)).takeWhile(_ != -1).foreach(out.write(buffer, 0, _))

      println(s"======= Saving ${file.getName} in parquet format... =======")
      if (outFile.toString.toLowerCase.endsWith(".txt")) {
          val df: DataFrame = spark.read.text(outFile.toString)
          // Пишу на локальную машину, тк тестирую с нее
          df.write.mode("overwrite").parquet(parquetPath.toString.dropRight(4))
          // df.write.parquet(s"hdfs://172.17.0.23:8020/user/a.surzhikov/$parquetPath.toString.dropRight(4)")
          println(s"======= ${file.getName} successfully saved =======")
        } else if (outFile.toString.toLowerCase.endsWith(".xml")) {
          val xml: Elem = XML.load(outFile.toString)
          val rowTag: String = xml.child.head.toString.split(" ").head.substring(1)
          val sourceDf: DataFrame = spark.read.format("com.databricks.spark.xml")
            .option("rowTag", rowTag)
            .load(outFile.toString)
          val resDf: DataFrame = sourceDf.columns.foldLeft(sourceDf)((acc, col) => {
            acc.withColumnRenamed(col, col.toLowerCase())
          })
          // Пишу на локальную машину, тк запускаю с нее
          resDf.write.mode("overwrite").parquet(parquetPath.toString.dropRight(4))
          // resDf.write.mode("overwrite").parquet(s"hdfs://172.17.0.23:8020/user/a.surzhikov/$parquetPath.toString.dropRight(4)")
          println(s"======= ${file.getName} successfully saved =======")
        } else {
          println("======= Unexpected file type =======")
        }
      }
    }

  spark.stop()
}