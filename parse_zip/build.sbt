scalaVersion := "2.13.12"

name := "parse-zip"
organization := "ch.epfl.scala"
version := "1.0"


libraryDependencies ++= Seq("org.scala-lang.modules" %% "scala-parser-combinators" % "2.3.0",
                            "org.apache.spark" %% "spark-core" % "3.5.1",
                            "org.apache.spark" %% "spark-sql" % "3.5.1",
                            "com.databricks" %% "spark-xml" % "0.18.0"
                            )

