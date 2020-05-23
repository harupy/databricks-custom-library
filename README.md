# Databricks Custom Library

A template to develop a custom python library using Databricks REST API and GitHub Actions.

## Creating a development environment

```bash
conda create -n <env_name> python=3.7
pip install -r requirements-dev.txt
pip install -r requirements.txt
```

## Running lint check

```bash
flake8 .
black --check .
```

## Running tests

```bash
pytest
```

## Building documentation

```bash
cd docs
make html
```
