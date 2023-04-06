from jp_list import *
import pykakasi

def kanji_to_hiragana(text):
    # if not isinstance(text, str):
    #     raise TypeError("Input text should be a string.")
    # if not all(token in list(hiragana_to_english) for token in text):
    #     raise ValueError("Input text is not Japanese.")
    
    kakasi = pykakasi.kakasi()
    kakasi.setMode("J", "H")
    conv = kakasi.getConverter()
    text = conv.do(text)
    return text

def translit_jp(text):
    hiragana_to_english.update(katakana_to_english)
    transliterated_text = ""
    i = 0
    while i < len(text):
        if i < len(text) - 1 and text[i+1] in ['ッ', 'っ']:
            transliterated_text += hiragana_to_english[text[i]][0]
            i += 1
        else:
            transliterated_text += hiragana_to_english.get(text[i], text[i])
        i += 1
    return transliterated_text

while True:
    input_text = input("Please enter Japanese text: ")
    hiragana_text = kanji_to_hiragana(input_text)
    print(translit_jp(hiragana_text))