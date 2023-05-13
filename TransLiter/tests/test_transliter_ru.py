import pytest
from TransLiter.transliter_cyrillic import *

@pytest.mark.parametrize(
    "case, expected",
    [
        ("", ""),
        ("Привет", "Privet"),
        ("Спасибо", "Spasibo"),
        ("Добро пожаловать", "Dobro pozhalovat'"),
        ("Кошка", "Koshka"),
        ("Я люблю тебя", "YA lyublyu tebya"),
        ("Москва", "Moskva"),
        ("Ресторан", "Restoran"),
        ("Солнце", "Solncze"),
        ("Здравствуйте", "Zdravstvujte"),
        ("Россия", "Rossiya")
    ],
)
def test_convert(case, expected):
    message = (f"returned {ru(case)} instead of {expected}")
    assert ru(case) == expected, message