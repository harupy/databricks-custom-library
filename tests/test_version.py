import dblib


def test_version_exists():
    assert hasattr(dblib, "__version__")
