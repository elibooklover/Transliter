import pytest
from TransLiter.transliter_ru import *

@pytest.mark.parametrize(
    "case, expected",
    [
        ("", ""),
    ],
)
def test_convert(case, expected):
    message = (f"returned {ru(case)} instead of {expected}")
    assert ru(case) == expected, message