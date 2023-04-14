import pytest
import TransLiter as tl

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
    message = (f"returned {tl.convert(case)} instead of {expected}")
    assert tl.convert(case) == expected, message

@pytest.mark.parametrize(
    "case, expected",
    [
        ("", ""),
        ("안녕하세요.","annyeohaseyo."),
        ("오늘 날씨 좋네요!", "oneur narssi johneyo!"),
        ("행복한 하루 되세요.", "haeboghan haru doeseyo."),
        ("저는 독서가 취미입니다.", "jeoneun dogseoga chwimiibnida."),
        ("하루하루 재미있게 살아요.", "haruharu jaemiissge sarayo."),
        ("가족들과 저녁을 먹어요.", "gajogdeurgwa jeonyeogeur meogeoyo.")
    ],
)
def test_ko(case, expected):
    message = (f"returned {tl.ko(case)} instead of {expected}")
    assert tl.ko(case) == expected, message
