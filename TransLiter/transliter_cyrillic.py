from TransLiter.cyrillic_list import *
import pandas as pd

# Russian
def ru(text):
    transliterated_text = ""
    for letter in text:
        try: 
            if letter in russian_list:
                transliterated_text += russian_list[letter]
            else:
                transliterated_text += letter
        except KeyError:
            pass
    return transliterated_text

# Serbian
def sr(text):
    transliterated_text = ""
    for letter in text:
        try: 
            if letter in serbian_list:
                transliterated_text += serbian_list[letter]
            else:
                transliterated_text += letter
        except KeyError:
            pass
    return transliterated_text

def transliter_ru():
    while True:
        input_text = input("Please enter Russian text: ")
        print(ru(input_text))
        if input_text == "": 
            break

def transliter_sr():
    while True:
        input_text = input("Please enter Serbian text: ")
        print(sr(input_text))
        if input_text == "": 
            break

def txt_ru(file):
    f = open(file, 'r')
    f2 = open("output_ru.txt", 'w')
    result = ""
    while True:
        line = f.readline()
        result += line + ru(line)
        if not line: 
            break
    print(result)
    f2.write(result)
    f.close()
    f2.close()

def txt_sr(file):
    f = open(file, 'r')
    f2 = open("output_sr.txt", 'w')
    result = ""
    while True:
        line = f.readline()
        result += line + sr(line)
        if not line: 
            break
    print(result)
    f2.write(result)
    f.close()
    f2.close()

def csv_ru(file):
    data = pd.DataFrame(columns=['Original Text', 'Transliterated Text'])
    f = open(file, 'r')
    lines = f.readlines()
    
    index_list = list(range(len(lines)))
    sentence_list = []
    transliter_list = []
    for sentence in lines:
        st = sentence.strip()
        tr = ru(st)
        sentence_list.append(st)
        transliter_list.append(tr)

    data = pd.DataFrame({'Original Text': sentence_list, 'Transliterated Text': transliter_list}, index=index_list)
    data.to_csv("output_ru.csv", encoding="utf-8-sig")
    print(data)
    f.close()

def csv_sr(file):
    data = pd.DataFrame(columns=['Original Text', 'Transliterated Text'])
    f = open(file, 'r')
    lines = f.readlines()
    
    index_list = list(range(len(lines)))
    sentence_list = []
    transliter_list = []
    for sentence in lines:
        st = sentence.strip()
        tr = sr(st)
        sentence_list.append(st)
        transliter_list.append(tr)

    data = pd.DataFrame({'Original Text': sentence_list, 'Transliterated Text': transliter_list}, index=index_list)
    data.to_csv("output_sr.csv", encoding="utf-8-sig")
    print(data)
    f.close()