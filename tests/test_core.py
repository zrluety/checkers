import checkers

import pandas as pd

from pandas import Series, DataFrame
from pandas.testing import assert_series_equal


def test_find_unique(tmpdir):
    # find_unique should detect that the Id column is unique and the other
    # columns are not.
    df = DataFrame(
        {
            "Id": [1, 2, 3, 4, 5],
            "First": ["Zachary", "Joseph", "Amanda", "Amanda", "Megan"],
            "Last": ["Luety", "Kirsits", "Kemling", "Lubking", "Luety"],
        }
    )

    expected = Series(data=[True, False, False], index=["Id", "First", "Last"])

    assert_series_equal(checkers.find_unique(df), expected)


def test_find_orphans():
    # find_orphans shoudld detect that Id 2 in datasetB, beloning to
    # a_Id 6, has no matching Id in datasetA.
    dataset_a = DataFrame(
        {"Name": ["Zachary", "Weston"], "Age": [27, 30]}, index=[1, 2]
    )

    dataset_b = DataFrame({"a_Id": [1, 6], "Amount": [100.00, 200.00]}, index=[1, 2])

    expected = Series(data=[True, False], index=[1, 2])

    assert_series_equal(
        checkers.find_orphans(dataset_a, dataset_b, fk="a_Id"), expected
    )


def test_find_partial_dates():
    # find_partial_dates should detect that EffectiveDate does not contain
    # data through valuation_date while OccurrenceDate does

    dataset = DataFrame(
        {
            "EffectiveDate": [pd.datetime(2018, 7, 1), pd.datetime(2018, 12, 15)],
            "OccurrenceDate": [pd.datetime(2018, 9, 30), pd.datetime(2018, 12, 31)],
        }
    )
    valuation_date = pd.datetime(2018, 12, 31)

    expected = Series(data=[False, True], index=["EffectiveDate", "OccurrenceDate"])

    assert_series_equal(checkers.find_partial_dates(dataset, valuation_date), expected)
