import pytest
import TransLiter as tl

@pytest.mark.parametrize(
    "case, expected",
    [
        ("", ""),
        ("読書", "どくしょ"),
        ("運動", "うんどう"),
        ("遊園地", "ゆうえんち"),
        ("図書館", "としょかん")
    ],
)
def test_kanji_to_hiragana(case, expected):
    message = (f"returned {tl.kanji_to_hiragana(case)} instead of {expected}")
    assert tl.kanji_to_hiragana(case) == expected, message

@pytest.mark.parametrize(
    "case, expected",
    [
        ("", ""),
        ("気を付けて。", "kiwotsukete。"),
        ("良いニュースです。", "yoinyuーsudesu。"),
        ("おやすみなさい。", "oyasuminasai。"),
        ("おねがいします。", "onegaishimasu。"),
        ("気をつけてください。", "kiwotsuketekudasai。"),
        ("それはいい考えですね。", "sorehaiikangaedesune。")
    ],
)
def test_jp(case, expected):
    message = (f"returned {tl.jp(case)} instead of {expected}")
    assert tl.jp(case) == expected, message
