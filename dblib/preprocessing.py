from pyspark.sql import functions as F


def add_one(df, col):
    """
    Add one to a specified column.

    Parameters
    ----------
    df : Spark DataFrame
    col : str
        A column to add one to. Must be numeric.

    Returns
    -------
    Spark DataFrame
        A new dataframe with an updated column.

    Examples
    --------
    >>> df = spark.createDataFrame([(0,), (1,)], ["x"])
    >>> add_one(df, "x").show()  # doctest: +NORMALIZE_WHITESPACE
    +---+
    |  x|
    +---+
    |  1|
    |  2|
    +---+

    """
    return df.withColumn(col, F.col(col) + 1)
