from arabic_list import *
import pandas as pd

def ar(text, region=None):
    if region is None:
        transliterated_text = ""
        for letter in text:
            try: 
                if letter in ARABIC_TO_BUCKWALTER:
                    transliterated_text += ARABIC_TO_BUCKWALTER[letter]
                else:
                    transliterated_text += letter
            except KeyError:
                pass
        return transliterated_text
    elif region == 'tn':
        transliterated_text = ""
        for letter in text:
            try: 
                if letter in TUNISIAN_ARABIC:
                    transliterated_text += TUNISIAN_ARABIC[letter]
                else:
                    transliterated_text += letter
            except KeyError:
                pass
        return transliterated_text
    else:
        raise ValueError("Please enter proper values.")

def transliter_ar():
    while True:
        input_text = input("Please enter Russian text: ")
        print(ar(input_text))
        if input_text == "": 
            break

def txt_ar(file):
    f = open(file, 'r')
    f2 = open("output_ar.txt", 'w')
    result = ""
    while True:
        line = f.readline()
        result += line + ar(line)
        if not line: 
            break
    print(result)
    f2.write(result)
    f.close()
    f2.close()

def csv_ar(file):
    data = pd.DataFrame(columns=['Original Text', 'Transliterated Text'])
    f = open(file, 'r')
    lines = f.readlines()
    
    index_list = list(range(len(lines)))
    sentence_list = []
    transliter_list = []
    for sentence in lines:
        st = sentence.strip()
        tr = ar(st)
        sentence_list.append(st)
        transliter_list.append(tr)

    data = pd.DataFrame({'Original Text': sentence_list, 'Transliterated Text': transliter_list}, index=index_list)
    data.to_csv("output_ar.csv", encoding="utf-8-sig")
    print(data)
    f.close()