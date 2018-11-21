import pandas as pd

from pandas import DataFrame, Series


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


def find_partial_dates(data: DataFrame, valuation_date: pd.datetime) -> Series:
    """Find columns that dont have values through valuation_date."""
    return Series(
        data=[
            data[column].max().to_pydatetime() == valuation_date
            for column in data.columns
        ],
        index=data.columns,
    )
