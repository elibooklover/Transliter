import os
import pandas as pd
from transliter.transliter_jp import *
from transliter.transliter_ko import *
from transliter.transliter_cyrillic import *

class Transliterator:
    def __init__(self, language):
        self.language = language
        
    def transliter2(self):
        while True:
            input_text = input(f"Please enter {self.language} text: ")
            if input_text == "":
                break
            if self.language == "Korean":
                print(ko(input_text))
            elif self.language == "Japanese":
                print(jp(input_text))
            elif self.language == "Russian":
                print(ru(input_text))
            elif self.language == "Ukrainian":
                print(ua(input_text))
            elif self.language == "Bulgarian":
                print(bg(input_text))
            elif self.language == "Macedonian":
                print(mk(input_text))
            elif self.language == "Mongolian":
                print(mn(input_text))
            elif self.language == "Montenegrin":
                print(me(input_text))
            elif self.language == "Serbian":
                print(sr(input_text))
            elif self.language == "Tajiki":
                print(tj(input_text))

    def export_txt(self, language_code, file):
        f = open(file, 'r')
        new_file = os.path.splitext(file)[0]
        f2 = open(f"{new_file}_output.txt", 'w')
        result = ""
        while True:
            line = f.readline()
            result += line + language_code(line)
            if not line: 
                break
        print(result)
        f2.write(result)
        f.close()
        f2.close()
    
    def export_csv(self, language_code, file):
        data = pd.DataFrame(columns=['Original Text', 'Transliterated Text'])
        f = open(file, 'r')
        new_file = os.path.splitext(file)[0]
        lines = f.readlines()
        
        index_list = list(range(len(lines)))
        sentence_list = []
        transliter_list = []
        for sentence in lines:
            st = sentence.strip()
            tr = language_code(st)
            sentence_list.append(st)
            transliter_list.append(tr)

        data = pd.DataFrame({'Original Text': sentence_list, 'Transliterated Text': transliter_list}, index=index_list)
        data.to_csv(f"{new_file}_output.csv", encoding="utf-8-sig")
        print(data)
        f.close()

def transliter_ko():
    transliter = Transliterator("Korean")
    return transliter.transliter2()

def transliter_jp():
    transliter = Transliterator("Japanese")
    return transliter.transliter2()

def transliter_ru():
    transliter = Transliterator("Russian")
    return transliter.transliter2()

def transliter_ua():
    transliter = Transliterator("Ukrainian")
    return transliter.transliter2()

def transliter_bg():
    transliter = Transliterator("Bulgarian")
    return transliter.transliter2()

def transliter_mk():
    transliter = Transliterator("Macedonian")
    return transliter.transliter2()

def transliter_mn():
    transliter = Transliterator("Mongolian")
    return transliter.transliter2()

def transliter_me():
    transliter = Transliterator("Montenegrin")
    return transliter.transliter2()

def transliter_sr():
    transliter = Transliterator("Serbian")
    return transliter.transliter2()

def transliter_tj():
    transliter = Transliterator("Tajiki")
    return transliter.transliter2()

def txt_ko(file):
    transliter = Transliterator("Korean")
    return transliter.export_txt(ko, file)

def txt_jp(file):
    transliter = Transliterator("Japanese")
    return transliter.export_txt(jp, file)

def txt_ru(file):
    transliter = Transliterator("Russian")
    return transliter.export_txt(ru, file)

def txt_ua(file):
    transliter = Transliterator("Ukrainian")
    return transliter.export_txt(ua, file)

def txt_bg(file):
    transliter = Transliterator("Bulgarian")
    return transliter.export_txt(bg, file)

def txt_mk(file):
    transliter = Transliterator("Macedonian")
    return transliter.export_txt(mk, file)

def txt_mn(file):
    transliter = Transliterator("Mongolian")
    return transliter.export_txt(mn, file)

def txt_me(file):
    transliter = Transliterator("Montenegrin")
    return transliter.export_txt(me, file)

def txt_sr(file):
    transliter = Transliterator("Serbian")
    return transliter.export_txt(sr, file)

def txt_tj(file):
    transliter = Transliterator("Tajiki")
    return transliter.export_txt(tj, file)

def csv_ko(file):
    transliter = Transliterator("Korean")
    return transliter.export_csv(ko, file)

def csv_jp(file):
    transliter = Transliterator("Japanese")
    return transliter.export_csv(jp, file)

def csv_ru(file):
    transliter = Transliterator("Russian")
    return transliter.export_csv(ru, file)

def csv_ua(file):
    transliter = Transliterator("Ukrainian")
    return transliter.export_csv(ua, file)

def csv_bg(file):
    transliter = Transliterator("Bulgarian")
    return transliter.export_csv(bg, file)

def csv_mk(file):
    transliter = Transliterator("Macedonian")
    return transliter.export_csv(mk, file)

def csv_mn(file):
    transliter = Transliterator("Mongolian")
    return transliter.export_csv(mn, file)

def csv_me(file):
    transliter = Transliterator("Montenegrin")
    return transliter.export_csv(me, file)

def csv_sr(file):
    transliter = Transliterator("Serbian")
    return transliter.export_csv(sr, file)

def csv_tj(file):
    transliter = Transliterator("Tajiki")
    return transliter.export_csv(tj, file)
