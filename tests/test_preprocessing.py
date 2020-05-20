from dblib import preprocessing as pp
from dblib.testing.utils import create_session, assert_frame_equal


spark = create_session()


def test_add_one():
    df = spark.createDataFrame([(0,), (1,)], ["x"])
    actual = pp.add_one(df, "x")
    expected = spark.createDataFrame([(1,), (2,)], ["x"])
    assert_frame_equal(actual, expected)
