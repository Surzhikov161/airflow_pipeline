file://<WORKSPACE>/src/main/scala/Main.scala
### scala.reflect.internal.FatalError: class Object does not have a method getClass

occurred in the presentation compiler.

presentation compiler configuration:
Scala version: 2.13.12
Classpath:
<WORKSPACE>/.bloop/parse_zip/bloop-bsp-clients-classes/classes-Metals-1hyUlAo-QWiaZyjM5ICZrw== [exists ], <HOME>/.cache/bloop/semanticdb/com.sourcegraph.semanticdb-javac.0.9.10/semanticdb-javac-0.9.10.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/scala-library/2.13.12/scala-library-2.13.12.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/modules/scala-parser-combinators_2.13/2.3.0/scala-parser-combinators_2.13-2.3.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/spark/spark-sql_2.13/3.5.1/spark-sql_2.13-3.5.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/rocksdb/rocksdbjni/8.3.2/rocksdbjni-8.3.2.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/com/univocity/univocity-parsers/2.9.1/univocity-parsers-2.9.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/spark/spark-sketch_2.13/3.5.1/spark-sketch_2.13-3.5.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/spark/spark-core_2.13/3.5.1/spark-core_2.13-3.5.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/spark/spark-catalyst_2.13/3.5.1/spark-catalyst_2.13-3.5.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/spark/spark-tags_2.13/3.5.1/spark-tags_2.13-3.5.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/modules/scala-parallel-collections_2.13/1.0.4/scala-parallel-collections_2.13-1.0.4.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/orc/orc-core/1.9.2/orc-core-1.9.2-shaded-protobuf.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/orc/orc-mapreduce/1.9.2/orc-mapreduce-1.9.2-shaded-protobuf.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/hive/hive-storage-api/2.8.1/hive-storage-api-2.8.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/parquet/parquet-column/1.13.1/parquet-column-1.13.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/parquet/parquet-hadoop/1.13.1/parquet-hadoop-1.13.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/com/fasterxml/jackson/core/jackson-databind/2.15.2/jackson-databind-2.15.2.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/xbean/xbean-asm9-shaded/4.23/xbean-asm9-shaded-4.23.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/avro/avro/1.11.2/avro-1.11.2.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/avro/avro-mapred/1.11.2/avro-mapred-1.11.2.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/com/twitter/chill_2.13/0.10.0/chill_2.13-0.10.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/com/twitter/chill-java/0.10.0/chill-java-0.10.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/hadoop/hadoop-client-api/3.3.4/hadoop-client-api-3.3.4.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/hadoop/hadoop-client-runtime/3.3.4/hadoop-client-runtime-3.3.4.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/spark/spark-launcher_2.13/3.5.1/spark-launcher_2.13-3.5.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/spark/spark-kvstore_2.13/3.5.1/spark-kvstore_2.13-3.5.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/spark/spark-network-common_2.13/3.5.1/spark-network-common_2.13-3.5.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/spark/spark-network-shuffle_2.13/3.5.1/spark-network-shuffle_2.13-3.5.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/spark/spark-unsafe_2.13/3.5.1/spark-unsafe_2.13-3.5.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/spark/spark-common-utils_2.13/3.5.1/spark-common-utils_2.13-3.5.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/javax/activation/activation/1.1.1/activation-1.1.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/curator/curator-recipes/2.13.0/curator-recipes-2.13.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/zookeeper/zookeeper/3.6.3/zookeeper-3.6.3.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/jakarta/servlet/jakarta.servlet-api/4.0.3/jakarta.servlet-api-4.0.3.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/commons-codec/commons-codec/1.16.0/commons-codec-1.16.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/commons/commons-compress/1.23.0/commons-compress-1.23.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/commons/commons-lang3/3.12.0/commons-lang3-3.12.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/commons/commons-math3/3.6.1/commons-math3-3.6.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/commons/commons-text/1.10.0/commons-text-1.10.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/commons-io/commons-io/2.13.0/commons-io-2.13.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/commons-collections/commons-collections/3.2.2/commons-collections-3.2.2.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/commons/commons-collections4/4.4/commons-collections4-4.4.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/com/google/code/findbugs/jsr305/3.0.2/jsr305-3.0.2.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/com/ning/compress-lzf/1.1.2/compress-lzf-1.1.2.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/xerial/snappy/snappy-java/1.1.10.3/snappy-java-1.1.10.3.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/lz4/lz4-java/1.8.0/lz4-java-1.8.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/com/github/luben/zstd-jni/1.5.5-4/zstd-jni-1.5.5-4.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/roaringbitmap/RoaringBitmap/0.9.45/RoaringBitmap-0.9.45.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/modules/scala-xml_2.13/2.1.0/scala-xml_2.13-2.1.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/scala-lang/scala-reflect/2.13.12/scala-reflect-2.13.12.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/json4s/json4s-jackson_2.13/3.7.0-M11/json4s-jackson_2.13-3.7.0-M11.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/glassfish/jersey/core/jersey-client/2.40/jersey-client-2.40.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/glassfish/jersey/core/jersey-common/2.40/jersey-common-2.40.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/glassfish/jersey/core/jersey-server/2.40/jersey-server-2.40.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/glassfish/jersey/containers/jersey-container-servlet/2.40/jersey-container-servlet-2.40.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/glassfish/jersey/containers/jersey-container-servlet-core/2.40/jersey-container-servlet-core-2.40.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/glassfish/jersey/inject/jersey-hk2/2.40/jersey-hk2-2.40.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-all/4.1.96.Final/netty-all-4.1.96.Final.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-transport-native-epoll/4.1.96.Final/netty-transport-native-epoll-4.1.96.Final-linux-x86_64.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-transport-native-epoll/4.1.96.Final/netty-transport-native-epoll-4.1.96.Final-linux-aarch_64.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-transport-native-kqueue/4.1.96.Final/netty-transport-native-kqueue-4.1.96.Final-osx-aarch_64.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-transport-native-kqueue/4.1.96.Final/netty-transport-native-kqueue-4.1.96.Final-osx-x86_64.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/com/clearspring/analytics/stream/2.9.6/stream-2.9.6.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/io/dropwizard/metrics/metrics-core/4.2.19/metrics-core-4.2.19.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/io/dropwizard/metrics/metrics-jvm/4.2.19/metrics-jvm-4.2.19.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/io/dropwizard/metrics/metrics-json/4.2.19/metrics-json-4.2.19.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/io/dropwizard/metrics/metrics-graphite/4.2.19/metrics-graphite-4.2.19.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/io/dropwizard/metrics/metrics-jmx/4.2.19/metrics-jmx-4.2.19.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/com/fasterxml/jackson/module/jackson-module-scala_2.13/2.15.2/jackson-module-scala_2.13-2.15.2.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/ivy/ivy/2.5.1/ivy-2.5.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/oro/oro/2.0.8/oro-2.0.8.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/net/razorvine/pickle/1.3/pickle-1.3.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/net/sf/py4j/py4j/0.10.9.7/py4j-0.10.9.7.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/commons/commons-crypto/1.1.0/commons-crypto-1.1.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/spark/spark-sql-api_2.13/3.5.1/spark-sql-api_2.13-3.5.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/codehaus/janino/janino/3.1.9/janino-3.1.9.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/codehaus/janino/commons-compiler/3.1.9/commons-compiler-3.1.9.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/datasketches/datasketches-java/3.3.0/datasketches-java-3.3.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/orc/orc-shims/1.9.2/orc-shims-1.9.2.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/io/airlift/aircompressor/0.25/aircompressor-0.25.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/jetbrains/annotations/17.0.0/annotations-17.0.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/slf4j/slf4j-api/2.0.7/slf4j-api-2.0.7.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/threeten/threeten-extra/1.7.1/threeten-extra-1.7.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/parquet/parquet-common/1.13.1/parquet-common-1.13.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/parquet/parquet-encoding/1.13.1/parquet-encoding-1.13.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/yetus/audience-annotations/0.13.0/audience-annotations-0.13.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/parquet/parquet-format-structures/1.13.1/parquet-format-structures-1.13.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/parquet/parquet-jackson/1.13.1/parquet-jackson-1.13.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/com/fasterxml/jackson/core/jackson-annotations/2.15.2/jackson-annotations-2.15.2.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/com/fasterxml/jackson/core/jackson-core/2.15.2/jackson-core-2.15.2.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/avro/avro-ipc/1.11.2/avro-ipc-1.11.2.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/com/esotericsoftware/kryo-shaded/4.0.2/kryo-shaded-4.0.2.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/fusesource/leveldbjni/leveldbjni-all/1.8/leveldbjni-all-1.8.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/com/google/crypto/tink/tink/1.9.0/tink-1.9.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/slf4j/jul-to-slf4j/2.0.7/jul-to-slf4j-2.0.7.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/slf4j/jcl-over-slf4j/2.0.7/jcl-over-slf4j-2.0.7.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/logging/log4j/log4j-slf4j2-impl/2.20.0/log4j-slf4j2-impl-2.20.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/logging/log4j/log4j-api/2.20.0/log4j-api-2.20.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/logging/log4j/log4j-core/2.20.0/log4j-core-2.20.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/logging/log4j/log4j-1.2-api/2.20.0/log4j-1.2-api-2.20.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/curator/curator-framework/2.13.0/curator-framework-2.13.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/zookeeper/zookeeper-jute/3.6.3/zookeeper-jute-3.6.3.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/roaringbitmap/shims/0.9.45/shims-0.9.45.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/json4s/json4s-core_2.13/3.7.0-M11/json4s-core_2.13-3.7.0-M11.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/jakarta/ws/rs/jakarta.ws.rs-api/2.1.6/jakarta.ws.rs-api-2.1.6.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/glassfish/hk2/external/jakarta.inject/2.6.1/jakarta.inject-2.6.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/jakarta/annotation/jakarta.annotation-api/1.3.5/jakarta.annotation-api-1.3.5.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/glassfish/hk2/osgi-resource-locator/1.0.3/osgi-resource-locator-1.0.3.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/jakarta/validation/jakarta.validation-api/2.0.2/jakarta.validation-api-2.0.2.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/glassfish/hk2/hk2-locator/2.6.1/hk2-locator-2.6.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/javassist/javassist/3.29.2-GA/javassist-3.29.2-GA.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-buffer/4.1.96.Final/netty-buffer-4.1.96.Final.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-codec/4.1.96.Final/netty-codec-4.1.96.Final.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-codec-http/4.1.96.Final/netty-codec-http-4.1.96.Final.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-codec-http2/4.1.96.Final/netty-codec-http2-4.1.96.Final.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-codec-socks/4.1.96.Final/netty-codec-socks-4.1.96.Final.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-common/4.1.96.Final/netty-common-4.1.96.Final.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-handler/4.1.96.Final/netty-handler-4.1.96.Final.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-transport-native-unix-common/4.1.96.Final/netty-transport-native-unix-common-4.1.96.Final.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-handler-proxy/4.1.96.Final/netty-handler-proxy-4.1.96.Final.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-resolver/4.1.96.Final/netty-resolver-4.1.96.Final.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-transport/4.1.96.Final/netty-transport-4.1.96.Final.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-transport-classes-epoll/4.1.96.Final/netty-transport-classes-epoll-4.1.96.Final.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-transport-classes-kqueue/4.1.96.Final/netty-transport-classes-kqueue-4.1.96.Final.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/com/thoughtworks/paranamer/paranamer/2.8/paranamer-2.8.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/antlr/antlr4-runtime/4.9.3/antlr4-runtime-4.9.3.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/arrow/arrow-vector/12.0.1/arrow-vector-12.0.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/arrow/arrow-memory-netty/12.0.1/arrow-memory-netty-12.0.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/datasketches/datasketches-memory/2.1.0/datasketches-memory-2.1.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/tukaani/xz/1.9/xz-1.9.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/com/esotericsoftware/minlog/1.3.0/minlog-1.3.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/objenesis/objenesis/2.5.1/objenesis-2.5.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/com/google/code/gson/gson/2.10.1/gson-2.10.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/com/google/protobuf/protobuf-java/3.19.6/protobuf-java-3.19.6.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/joda-time/joda-time/2.12.5/joda-time-2.12.5.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/curator/curator-client/2.13.0/curator-client-2.13.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/json4s/json4s-ast_2.13/3.7.0-M11/json4s-ast_2.13-3.7.0-M11.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/json4s/json4s-scalap_2.13/3.7.0-M11/json4s-scalap_2.13-3.7.0-M11.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/glassfish/hk2/external/aopalliance-repackaged/2.6.1/aopalliance-repackaged-2.6.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/glassfish/hk2/hk2-api/2.6.1/hk2-api-2.6.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/glassfish/hk2/hk2-utils/2.6.1/hk2-utils-2.6.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/arrow/arrow-format/12.0.1/arrow-format-12.0.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/org/apache/arrow/arrow-memory-core/12.0.1/arrow-memory-core-12.0.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/com/fasterxml/jackson/datatype/jackson-datatype-jsr310/2.15.1/jackson-datatype-jsr310-2.15.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/com/google/flatbuffers/flatbuffers-java/1.12.0/flatbuffers-java-1.12.0.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/com/google/guava/guava/16.0.1/guava-16.0.1.jar [exists ], <HOME>/.cache/coursier/v1/https/repo1.maven.org/maven2/io/netty/netty-transport-native-epoll/4.1.96.Final/netty-transport-native-epoll-4.1.96.Final.jar [exists ]
Options:
-release 11


action parameters:
offset: 822
uri: file://<WORKSPACE>/src/main/scala/Main.scala
text:
```scala
import org.apache.hadoop.conf.Configuration
import org.apache.hadoop.fs.{FileSystem, Path}
import java.net.URI
import scala.collection.immutable.Stream
import java.util.zip.{ZipFile, ZipEntry, ZipInputStream}
import org.apache.spark.sql.SparkSession
import scala.collection.JavaConverters._
import java.nio.file.{Files, Path, Paths, StandardCopyOption}
import java.nio.file.FileAlreadyExistsException

import scala.xml.XML

// "hdfs://172.17.0.23:8020/user/r.gazikhanov/angryjob/employees.csv"

object Main extends App {

  val spark = SparkSession.builder
    .appName("Simple Application")
    .master("local[8]")
    .config("spark.master", "local")
    .getOrCreate()


  val hdfs = FileSystem.get(new URI("hdfs://172.17.0.23:8020/user/a.surzhikov/"), new Configuration()) 
  val path = new org.apache.hadoop.fs.Path("@@/path/to/file/")
  val stream = hdfs.open(path)

  val zis: ZipInputStream = new ZipInputStream(stream)
  
  val unzip_dir = Paths.get("unzip_gar")
  val outputParsedPath = Paths.get("parsed_gar")


  Stream.continually(zis.getNextEntry).takeWhile(_ != null).foreach { file =>
    if (!file.isDirectory) {
      val outPath = unzip_dir.resolve(file.getName)
      val outPathParent = outPath.getParent
      if (!outPathParent.toFile.exists()) {
        outPathParent.toFile.mkdirs()
      }

      val outFile = outPath.toFile
      val out = new java.io.FileOutputStream(outFile)
      val buffer = new Array[Byte](4096)
      Stream.continually(zis.read(buffer)).takeWhile(_ != -1).foreach(out.write(buffer, 0, _))
    }

  
  val zip_path:String = "../../GAR/gar_xml.zip"
  val rootzip: ZipFile = new ZipFile(zip_path)
  

  // for (entry <- rootzip.entries.asScala) {

  //   val path = unzip_dir.resolve(entry.getName)
  //   val parquetPath = outputParsedPath.resolve(entry.getName)
  //   if (entry.isDirectory) {
  //     Files.createDirectories(path)
      
  //   } else {

  //     try {
  //       println(s"========= Trying to read $path =========")
  //       Files.createDirectories(path.getParent)
  //       Files.copy(rootzip.getInputStream(entry), path)
  //     }
  //     catch {
  //       case exception: FileAlreadyExistsException => println("========= File already exists =========")

  //     } finally {
  //       if (path.toString.endsWith(".txt")) {
  //         val df = spark.read.text(path.toString)
  //         df.write.parquet(parquetPath.toString)
  //       } else {
  //         val xml = XML.load(path.toString)
  //         val rowTag = xml.child.head.toString.split(" ").head.substring(1)
  //         val sourceDf = spark.read.format("com.databricks.spark.xml")
  //           .option("rowTag", rowTag)
  //           .load(path.toString)
  //         val resDf = sourceDf.columns.foldLeft(sourceDf)((acc, col) => {
  //           acc.withColumnRenamed(col, col.toLowerCase())
  //         })
  //         resDf.write.parquet(parquetPath.toString)
  //       // val df = spark.read.format("xml").load(path.toString)
  //       }
  //     }
    
  //   }
  // }
  spark.stop()
}}
```



#### Error stacktrace:

```
scala.reflect.internal.Definitions$DefinitionsClass.fatalMissingSymbol(Definitions.scala:1411)
	scala.reflect.internal.Definitions$DefinitionsClass.miss$1(Definitions.scala:1464)
	scala.reflect.internal.Definitions$DefinitionsClass.$anonfun$getMemberMethod$2(Definitions.scala:1466)
	scala.reflect.internal.Definitions$DefinitionsClass.getMemberMethod(Definitions.scala:1466)
	scala.reflect.internal.Definitions$DefinitionsClass.Any_getClass$lzycompute(Definitions.scala:1172)
	scala.reflect.internal.Definitions$DefinitionsClass.Any_getClass(Definitions.scala:1172)
	scala.reflect.internal.Definitions$DefinitionsClass.syntheticCoreMethods$lzycompute(Definitions.scala:1578)
	scala.reflect.internal.Definitions$DefinitionsClass.syntheticCoreMethods(Definitions.scala:1572)
	scala.reflect.internal.Definitions$DefinitionsClass.symbolsNotPresentInBytecode$lzycompute(Definitions.scala:1603)
	scala.reflect.internal.Definitions$DefinitionsClass.symbolsNotPresentInBytecode(Definitions.scala:1603)
	scala.reflect.internal.Definitions$DefinitionsClass.init(Definitions.scala:1659)
	scala.tools.nsc.Global$Run.<init>(Global.scala:1249)
	scala.tools.nsc.interactive.Global$TyperRun.<init>(Global.scala:1352)
	scala.tools.nsc.interactive.Global.newTyperRun(Global.scala:1375)
	scala.tools.nsc.interactive.Global.<init>(Global.scala:294)
	scala.meta.internal.pc.MetalsGlobal.<init>(MetalsGlobal.scala:40)
	scala.meta.internal.pc.ScalaPresentationCompiler.newCompiler(ScalaPresentationCompiler.scala:453)
```
#### Short summary: 

scala.reflect.internal.FatalError: class Object does not have a method getClass