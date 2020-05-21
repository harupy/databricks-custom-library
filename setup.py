import os
from setuptools import find_packages, setup

import dblib

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))


def get_readme():
    with open(os.path.join(ROOT_DIR, "README.md"), encoding="utf-8") as f:
        return f.read()


def get_install_requires():
    with open(os.path.join(ROOT_DIR, "requirements.txt"), encoding="utf-8") as f:
        return [
            line.strip()
            for line in f.readlines()
            if not (line.startswith("#") or (line.strip() == ""))
        ]


setup(
    name="dblib",
    version=dblib.__version__,
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=get_install_requires(),
    description="Databricks custom library",
    long_description=get_readme(),
    long_description_content_type="text/markdown",
)
