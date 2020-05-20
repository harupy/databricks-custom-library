from pyspark.sql import SparkSession


def create_session():
    return SparkSession.builder.appName("dblib").getOrCreate()
