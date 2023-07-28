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

def transliter_jp():
    while True:
        input_text = input("Please enter Japanese text: ")
        print(jp(input_text))
        if input_text == "": 
            break

def txt_jp(file):
    f = open(file, 'r')
    new_file = os.path.splitext(file)[0]
    f2 = open(f"{new_file}_output.txt", 'w')
    result = ""
    while True:
        line = f.readline()
        result += line + jp(line)
        if not line: 
            break
    print(result)
    f2.write(result)
    f.close()
    f2.close()

def csv_jp(file):
    data = pd.DataFrame(columns=['Original Text', 'Transliterated Text'])
    f = open(file, 'r')
    new_file = os.path.splitext(file)[0]
    lines = f.readlines()
    
    index_list = list(range(len(lines)))
    sentence_list = []
    transliter_list = []
    for sentence in lines:
        st = sentence.strip()
        tr = jp(st)
        sentence_list.append(st)
        transliter_list.append(tr)

    data = pd.DataFrame({'Original Text': sentence_list, 'Transliterated Text': transliter_list}, index=index_list)
    data.to_csv(f"{new_file}_output.csv", encoding="utf-8-sig")
    print(data)
    f.close()