import pytest
from TransLiter.transliter_cyrillic import *

@pytest.mark.parametrize(
    "case, expected",
    [
        ("", ""),
        ("Здраво", "Zdravo"),
        ("Хвала", "Hvala"),
        ("Добродошли", "Dobrodošli"),
        ("Мачка", "Mačka"),
        ("Волим те", "Volim te"),
        ("Београд", "Beograd"),
        ("Ресторан", "Restoran"),
        ("Сунце", "Sunce"),
        ("Ћирилица", "Ćirilica"),
        ("Србија", "Srbija")
    ],
)

def test_convert(case, expected):
    message = (f"returned {sr(case)} instead of {expected}")
    assert sr(case) == expected, message