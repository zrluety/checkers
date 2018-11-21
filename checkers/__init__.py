from pandas import Series, DataFrame


def find_unique(data: DataFrame) -> Series:
    """Find columns containing unique values."""
    return Series(
        data=[data[data.duplicated([column])].empty for column in data.columns],
        index=data.columns,
    )


def find_orphans(left: DataFrame, right: DataFrame, fk: str) -> Series:
    """Find records in right without a parent record in left using key."""
    inner_join = right.join(left, on=fk, how="inner")

    return Series(data=right.index.isin(inner_join.index), index=right.index)
