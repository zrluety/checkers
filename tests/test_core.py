import textwrap

import pytest

import checkers

def test_find_unique(tmpdir):
    """Looks for a unique id column in the data."""
    content = textwrap.dedent("""\
    Id,FirstName,LastName
    1,Zachary,Luety
    2,Joseph,Kirsits
    3,Amanda,Kemling
    4,Amanda,Lubking
    5,Megan,Luety
    """)

    p = tmpdir.mkdir("data").join("data.csv")
    p.write(content)

    # find_unique() should return True since the Id column is unique
    assert checkers.find_unique(p.strpath)
