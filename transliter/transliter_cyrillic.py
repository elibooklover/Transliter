from transliter.cyrillic_list import *
import pandas as pd
import os

class TransliterCyrillic:
    def __init__(self, language_list):
        self.language_list = language_list

    def transliter1(self, text):
        transliterated_text = ""
        for letter in text:
            try:
                if letter in self.language_list:
                    transliterated_text += self.language_list[letter]
                else:
                    transliterated_text += letter
            except KeyError:
                pass
        return transliterated_text
    
    def transliter2(self, transliterator, prompt):
        while True:
            input_text = input(prompt)
            if input_text == "":
                break
            print(transliterator(input_text))

    def export_txt(self, transliterator, file):
        f = open(file, 'r')
        new_file = os.path.splitext(file)[0]
        f2 = open(f"{new_file}_output.txt", 'w')
        result = ""
        while True:
            line = f.readline()
            result += line + transliterator(line)
            if not line: 
                break
        print(result)
        f2.write(result)
        f.close()
        f2.close()
    
    def export_csv(self, transliterator, file):
        data = pd.DataFrame(columns=['Original Text', 'Transliterated Text'])
        f = open(file, 'r')
        new_file = os.path.splitext(file)[0]
        lines = f.readlines()
        
        index_list = list(range(len(lines)))
        sentence_list = []
        transliter_list = []
        for sentence in lines:
            st = sentence.strip()
            tr = transliterator(st)
            sentence_list.append(st)
            transliter_list.append(tr)

        data = pd.DataFrame({'Original Text': sentence_list, 'Transliterated Text': transliter_list}, index=index_list)
        data.to_csv(f"{new_file}_output.csv", encoding="utf-8-sig")
        print(data)
        f.close()

def ru(text):
    transliterator = TransliterCyrillic(RUSSIAN_LIST)
    return transliterator.transliter1(text)

def ua(text):
    transliter = TransliterCyrillic(UKRAINIAN_LIST)
    return transliter.transliter1(text)

def bg(text):
    transliter = TransliterCyrillic(BULGARIAN_LIST)
    return transliter.transliter1(text)

def mk(text):
    transliter = TransliterCyrillic(MACEDONIAN_LIST)
    return transliter.transliter1(text)

def mn(text):
    transliter = TransliterCyrillic(MONGOLIAN_LIST)
    return transliter.transliter1(text)

def me(text):
    transliter = TransliterCyrillic(MONTENEGRIN_LIST)
    return transliter.transliter1(text)

def sr(text):
    transliter = TransliterCyrillic(SERBIAN_LIST)
    return transliter.transliter1(text)

def tj(text):
    transliter = TransliterCyrillic(TAJIKI_LIST)
    return transliter.transliter1(text)

def transliter_ru():
    transliter = TransliterCyrillic(RUSSIAN_LIST)
    return transliter.transliter2(ru, "Please enter Russian text: ")

def transliter_ua():
    transliter = TransliterCyrillic(UKRAINIAN_LIST)
    return transliter.transliter2(ua, "Please enter Ukrainian text: ")

def transliter_bg():
    transliter = TransliterCyrillic(BULGARIAN_LIST)
    return transliter.transliter2(bg, "Please enter Bulgarian text: ")

def transliter_mk():
    transliter = TransliterCyrillic(MACEDONIAN_LIST)
    return transliter.transliter2(mk, "Please enter Macedonian text: ")

def transliter_mn():
    transliter = TransliterCyrillic(MONGOLIAN_LIST)
    return transliter.transliter2(mk, "Please enter Mongolian text: ")

def transliter_me():
    transliter = TransliterCyrillic(MONTENEGRIN_LIST)
    return transliter.transliter2(mk, "Please enter Montenegrin text: ")

def transliter_sr():
    transliter = TransliterCyrillic(SERBIAN_LIST)
    return transliter.transliter2(mk, "Please enter Serbian text: ")

def transliter_tj():
    transliter = TransliterCyrillic(TAJIKI_LIST)
    return transliter.transliter2(mk, "Please enter Tajiki text: ")

def txt_ru(file):
    transliter = TransliterCyrillic(RUSSIAN_LIST)
    return transliter.export_txt(ru, file)

def txt_ua(file):
    transliter = TransliterCyrillic(UKRAINIAN_LIST)
    return transliter.export_txt(ua, file)

def txt_bg(file):
    transliter = TransliterCyrillic(BULGARIAN_LIST)
    return transliter.export_txt(bg, file)

def txt_mk(file):
    transliter = TransliterCyrillic(MACEDONIAN_LIST)
    return transliter.export_txt(mk, file)

def txt_mn(file):
    transliter = TransliterCyrillic(MONGOLIAN_LIST)
    return transliter.export_txt(mn, file)

def txt_me(file):
    transliter = TransliterCyrillic(MONTENEGRIN_LIST)
    return transliter.export_txt(me, file)

def txt_sr(file):
    transliter = TransliterCyrillic(SERBIAN_LIST)
    return transliter.export_txt(sr, file)

def txt_tj(file):
    transliter = TransliterCyrillic(TAJIKI_LIST)
    return transliter.export_txt(tj, file)

def csv_ru(file):
    transliter = TransliterCyrillic(RUSSIAN_LIST)
    return transliter.export_csv(ru, file)

def csv_ua(file):
    transliter = TransliterCyrillic(UKRAINIAN_LIST)
    return transliter.export_csv(ua, file)

def csv_bg(file):
    transliter = TransliterCyrillic(BULGARIAN_LIST)
    return transliter.export_csv(bg, file)

def csv_mk(file):
    transliter = TransliterCyrillic(MACEDONIAN_LIST)
    return transliter.export_csv(mk, file)

def csv_mn(file):
    transliter = TransliterCyrillic(MONGOLIAN_LIST)
    return transliter.export_csv(mn, file)

def csv_me(file):
    transliter = TransliterCyrillic(MONTENEGRIN_LIST)
    return transliter.export_csv(me, file)

def csv_sr(file):
    transliter = TransliterCyrillic(SERBIAN_LIST)
    return transliter.export_csv(sr, file)

def csv_tj(file):
    transliter = TransliterCyrillic(TAJIKI_LIST)
    return transliter.export_csv(tj, file)
