import pytest
from TransLiter.transliter_ko import *

@pytest.mark.parametrize(
    "case, expected",
    [
        ("", ""),
        ("하이", "ㅎㅏㅇㅣ"),
        ("안녕하세요.","ㅇㅏㄴㄴㅕㅇㅎㅏㅅㅔㅇㅛ."),
        ("오늘 날씨 좋네요!", "ㅇㅗㄴㅡㄹ ㄴㅏㄹㅆㅣ ㅈㅗㅎㄴㅔㅇㅛ!"),
        ("행복한 하루 되세요.", "ㅎㅐㅇㅂㅗㄱㅎㅏㄴ ㅎㅏㄹㅜ ㄷㅚㅅㅔㅇㅛ."),
        ("저는 독서가 취미입니다.", "ㅈㅓㄴㅡㄴ ㄷㅗㄱㅅㅓㄱㅏ ㅊㅟㅁㅣㅇㅣㅂㄴㅣㄷㅏ."),
        ("하루하루 재미있게 살아요.", "ㅎㅏㄹㅜㅎㅏㄹㅜ ㅈㅐㅁㅣㅇㅣㅆㄱㅔ ㅅㅏㄹㅇㅏㅇㅛ."),
        ("가족들과 저녁을 먹어요.", "ㄱㅏㅈㅗㄱㄷㅡㄹㄱㅘ ㅈㅓㄴㅕㄱㅇㅡㄹ ㅁㅓㄱㅇㅓㅇㅛ.")
    ],
)
def test_convert(case, expected):
    message = (f"returned {convert(case)} instead of {expected}")
    assert convert(case) == expected, message

@pytest.mark.parametrize(
    "case, expected",
    [
        ("", ""),
        ("안녕하세요.","annyeonghaseyo."),
        ("오늘 날씨 좋네요!", "oneul nalssi jotneyo!"),
        ("행복한 하루 되세요.", "haengbokhan haru doeseyo."),
        ("저는 독서가 취미입니다.", "jeoneun dokseoga chwimiibnida."),
        ("하루하루 재미있게 살아요.", "haruharu jaemiitge salayo."),
        ("가족들과 저녁을 먹어요.", "gajokdeulgwa jeonyeokeul meokeoyo.")
    ],
)
def test_ko(case, expected):
    message = (f"returned {ko(case)} instead of {expected}")
    assert ko(case) == expected, message
