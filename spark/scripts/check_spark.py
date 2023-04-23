
import findspark
findspark.init()

from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.master("local")
    .appName("IcebergPySpark")
    .config("spark.jars", "/home/asus/Downloads/iceberg-spark-runtime-3.2_2.12-1.2.0.jar")
    .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions")
    .config("spark.sql.catalog.demo", "org.apache.iceberg.spark.SparkCatalog")
    .config("spark.sql.catalog.demo.catalog-impl", "org.apache.iceberg.rest.RESTCatalog")
    .config("spark.sql.catalog.demo.uri", "http://rest:8181")
    .config("spark.sql.catalog.demo.warehouse", "s3a://warehouse/wh/")
    .config("spark.sql.catalog.demo.s3.endpoint", "http://minio:9000")
    .config("spark.sql.defaultCatalog", "demo")
    .config("spark.eventLog.enabled", "true")
    .config("spark.eventLog.dir", "/home/iceberg/spark-events")
    .config("spark.history.fs.logDirectory", "/home/iceberg/spark-events")
    .config("spark.sql.catalogImplementation", "/home/iceberg/spark-events")
    .getOrCreate()
)