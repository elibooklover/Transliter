import pytest
from TransLiter.transliter_cyrillic import *

# Russian
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
def test_ru(case, expected):
    message = (f"returned {ru(case)} instead of {expected}")
    assert ru(case) == expected, message

# Ukrainian
@pytest.mark.parametrize(
    "case, expected",
    [
        ("", ""),
        ("Добрий день!", "Dobryj den'!"),
        ("Ласкаво просимо!", "Laskavo prosymo!"),
        ("Будь ласка", "Bud' laska"),
        ("Дякую", "Djakuju")
    ],
)
def test_ua(case, expected):
    message = (f"returned {ua(case)} instead of {expected}")
    assert ua(case) == expected, message

# Bulgarian
@pytest.mark.parametrize(
    "case, expected",
    [
        ("", ""),
        ("Здравейте", "Zdraveyte"),
        ("Благодаря", "Blagodarya"),
        ("Извинете", "Izvinete"),
        ("Колко струва?", "Kolko struva?"),
        ("Къде е тоалетната?", "Kăde e toaletnata?"),
        ("Как се казвате?", "Kak se kazvate?"),
        ("Радвам се да ви срещна", "Radvam se da vi sreshtna")
    ],
)
def test_bg(case, expected):
    message = (f"returned {bg(case)} instead of {expected}")
    assert bg(case) == expected, message

# Montenegrin
@pytest.mark.parametrize(
    "case, expected",
    [
        ("", ""),
        ("Здраво", "Zdravo"),
        ("Како сте?", "Kako ste?"),
        ("Како се зовете?", "Kako se zovete?"),
        ("Драго ми је", "Drago mi je"),
        ("Хвала", "Hvala")
    ],
)
def test_me(case, expected):
    message = (f"returned {me(case)} instead of {expected}")
    assert me(case) == expected, message

# Macedonian
@pytest.mark.parametrize(
    "case, expected",
    [
        ("", ""),
        ("Здраво", "Zdravo"),
        ("Добро утро", "Dobro utro"),
        ("Како сте?", "Kako ste?"),
        ("Како се викате?", "Kako se vikate?"),
        ("Мило ми е што ве запознав", "Milo mi e što ve zapoznav")
    ],
)
def test_mk(case, expected):
    message = (f"returned {mk(case)} instead of {expected}")
    assert mk(case) == expected, message

# Serbian
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
def test_sr(case, expected):
    message = (f"returned {sr(case)} instead of {expected}")
    assert sr(case) == expected, message

# Tajiki
@pytest.mark.parametrize(
    "case, expected",
    [
        ("", ""),
        ("Салом", "Salom"),
        ("Ташаккур", "Tašakkur"),
        ("Бародарӣ кунед", "Barodarī kuned"),
        ("Мутмаинам", "Mutmainam"),
        ("Шумо чӣ хеле кӯшед?", "Šumo čī hele kūšed?"),
        ("Мумкин аст ки шумо кумакам кунед?", "Mumkin ast ki šumo kumakam kuned?"),
        ("Тоалет дар куҷост?", "Toalet dar kuçost?")
    ],
)
def test_tj(case, expected):
    message = (f"returned {tj(case)} instead of {expected}")
    assert tj(case) == expected, message