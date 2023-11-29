from transliter.jp_list import *
import pykakasi
import pandas as pd
import os

def kanji_to_hiragana(text):
    kks = pykakasi.kakasi()
    hiragana_text = ''
    for result in kks.convert(text):
        if result['hira']:
            hiragana_text += result['hira']
        else:
            hiragana_text += result['orig']
    return hiragana_text

def jp(text):
    text = kanji_to_hiragana(text)
    HIRAGANA_TO_ENGLISH.update(KATAKANA_TO_ENGLISH)
    transliterated_text = ""
    i = 0
    while i < len(text):
        try:
            if i < len(text) - 1 and text[i+1] in ['ゃ', 'ゅ', 'ょ']:
                transliterated_text += HIRAGANA_TO_ENGLISH[text[i]+text[i+1]]
                i += 1
            else:
                transliterated_text += HIRAGANA_TO_ENGLISH.get(text[i], text[i])
        except KeyError:
            pass
        i += 1
    return transliterated_text
