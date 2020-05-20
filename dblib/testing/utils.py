from pandas import testing
from pyspark.sql import SparkSession


def assert_frame_equal(left, right):
    left = left.toPandas()
    right = right.toPandas()
    testing.assert_frame_equal(left, right)


def create_session():
    return SparkSession.builder.appName("dblib").getOrCreate()
