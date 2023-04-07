from jp_list import *
import pykakasi

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
    hiragana_to_english.update(katakana_to_english)
    transliterated_text = ""
    i = 0
    while i < len(text):
        if i < len(text) - 1 and text[i+1] in ['ッ', 'っ']:
            transliterated_text += hiragana_to_english[text[i]][0]
            i += 1
        elif i < len(text) - 1 and text[i+1] in ['ゃ', 'ゅ', 'ょ']:
            transliterated_text += hiragana_to_english[text[i]+text[i+1]]
            i += 1
        else:
            transliterated_text += hiragana_to_english.get(text[i], text[i])
        i += 1
    return transliterated_text

def transliter_jp():
    while True:
        input_text = input("Please enter Japanese text: ")
        print(jp(input_text))