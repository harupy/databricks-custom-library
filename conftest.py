import pytest

from dblib.testing.utils import create_session


spark = create_session()


@pytest.fixture(scope="session", autouse=True)
def session_termination():
    yield
    spark.stop()


@pytest.fixture(autouse=True)
def inject(doctest_namespace):
    doctest_namespace["spark"] = spark
