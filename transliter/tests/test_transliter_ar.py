import pytest
from transliter.transliter_ar import *

@pytest.mark.parametrize(
    "case, expected",
    [
        ("", ""),
        # ("الخيرصباح","sabah alkhayr"),
        # ("أنا أستمتع بتعلم لغات جديدة.","Ana astamti'u bi-ta'lim lughāt jadīdah."),
        # ("أين الحمام؟ ", "AynaAl hammam?"),
        # ("مندواعي سروري مقابلتك", "min dawaei sururi muqabalatuk"),
        # ("أتمنىلك يوم سعيد", "‘atamanaa lak yawm saeid")
    ],
)
def test_ko(case, expected):
    message = (f"returned {ar(case)} instead of {expected}")
    assert ar(case) == expected, message
