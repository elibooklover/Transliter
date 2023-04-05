from jp_list import *

def translit_jp(text):
    hiragana_to_english.update(katakana_to_english)
    # if not isinstance(text, str):
    #     raise TypeError("Input text should be a string.")
    # if not all(token in list(hiragana_to_english) for token in text):
    #     raise ValueError("Input text is not Japanese.")
     
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
    print(translit_jp(input_text))