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

# Ukrainian
def ua(text):
    transliterated_text = ""
    for letter in text:
        try: 
            if letter in ukrainian_list:
                transliterated_text += ukrainian_list[letter]
            else:
                transliterated_text += letter
        except KeyError:
            pass
    return transliterated_text

# Bulgarian
def bg(text):
    transliterated_text = ""
    for letter in text:
        try: 
            if letter in bulgarian_list:
                transliterated_text += bulgarian_list[letter]
            else:
                transliterated_text += letter
        except KeyError:
            pass
    return transliterated_text

# Macedonian
def mk(text):
    transliterated_text = ""
    for letter in text:
        try: 
            if letter in macedonian_list:
                transliterated_text += macedonian_list[letter]
            else:
                transliterated_text += letter
        except KeyError:
            pass
    return transliterated_text

# Montenegrin
def me(text):
    transliterated_text = ""
    for letter in text:
        try: 
            if letter in montenegrin_list:
                transliterated_text += montenegrin_list[letter]
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


# Trnasliter Function for each language
# Russian
def transliter_ru():
    while True:
        input_text = input("Please enter Russian text: ")
        print(ru(input_text))
        if input_text == "": 
            break

# Ukrainian
def transliter_ua():
    while True:
        input_text = input("Please enter Ukrainian text: ")
        print(ua(input_text))
        if input_text == "": 
            break

# Bulgarian
def transliter_bg():
    while True:
        input_text = input("Please enter Bulgarian text: ")
        print(bg(input_text))
        if input_text == "": 
            break

# Macedonian
def transliter_mk():
    while True:
        input_text = input("Please enter Macedonian text: ")
        print(mk(input_text))
        if input_text == "": 
            break

# Montenegrin
def transliter_me():
    while True:
        input_text = input("Please enter Montenegrin text: ")
        print(me(input_text))
        if input_text == "": 
            break

# Serbian
def transliter_sr():
    while True:
        input_text = input("Please enter Serbian text: ")
        print(sr(input_text))
        if input_text == "": 
            break

# Automatic generation of a txt file for each language
# Russian
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

# Ukrainian
def txt_ua(file):
    f = open(file, 'r')
    f2 = open("output_ua.txt", 'w')
    result = ""
    while True:
        line = f.readline()
        result += line + ua(line)
        if not line: 
            break
    print(result)
    f2.write(result)
    f.close()
    f2.close()

# Bulgarian
def txt_bg(file):
    f = open(file, 'r')
    f2 = open("output_bg.txt", 'w')
    result = ""
    while True:
        line = f.readline()
        result += line + bg(line)
        if not line: 
            break
    print(result)
    f2.write(result)
    f.close()
    f2.close()

# Macedonian
def txt_mk(file):
    f = open(file, 'r')
    f2 = open("output_mk.txt", 'w')
    result = ""
    while True:
        line = f.readline()
        result += line + mk(line)
        if not line: 
            break
    print(result)
    f2.write(result)
    f.close()
    f2.close()

# Montenegrin
def txt_me(file):
    f = open(file, 'r')
    f2 = open("output_me.txt", 'w')
    result = ""
    while True:
        line = f.readline()
        result += line + me(line)
        if not line: 
            break
    print(result)
    f2.write(result)
    f.close()
    f2.close()

# Serbian
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

# Automatic generation of a csv file for each language
# Russian
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

# Ukrainian
def csv_ua(file):
    data = pd.DataFrame(columns=['Original Text', 'Transliterated Text'])
    f = open(file, 'r')
    lines = f.readlines()
    
    index_list = list(range(len(lines)))
    sentence_list = []
    transliter_list = []
    for sentence in lines:
        st = sentence.strip()
        tr = ua(st)
        sentence_list.append(st)
        transliter_list.append(tr)

    data = pd.DataFrame({'Original Text': sentence_list, 'Transliterated Text': transliter_list}, index=index_list)
    data.to_csv("output_ua.csv", encoding="utf-8-sig")
    print(data)
    f.close()

# Bulgarian
def csv_bg(file):
    data = pd.DataFrame(columns=['Original Text', 'Transliterated Text'])
    f = open(file, 'r')
    lines = f.readlines()
    
    index_list = list(range(len(lines)))
    sentence_list = []
    transliter_list = []
    for sentence in lines:
        st = sentence.strip()
        tr = bg(st)
        sentence_list.append(st)
        transliter_list.append(tr)

    data = pd.DataFrame({'Original Text': sentence_list, 'Transliterated Text': transliter_list}, index=index_list)
    data.to_csv("output_bg.csv", encoding="utf-8-sig")
    print(data)
    f.close()

# Macedonian
def csv_mk(file):
    data = pd.DataFrame(columns=['Original Text', 'Transliterated Text'])
    f = open(file, 'r')
    lines = f.readlines()
    
    index_list = list(range(len(lines)))
    sentence_list = []
    transliter_list = []
    for sentence in lines:
        st = sentence.strip()
        tr = mk(st)
        sentence_list.append(st)
        transliter_list.append(tr)

    data = pd.DataFrame({'Original Text': sentence_list, 'Transliterated Text': transliter_list}, index=index_list)
    data.to_csv("output_mk.csv", encoding="utf-8-sig")
    print(data)
    f.close()

# Montenegrin
def csv_me(file):
    data = pd.DataFrame(columns=['Original Text', 'Transliterated Text'])
    f = open(file, 'r')
    lines = f.readlines()
    
    index_list = list(range(len(lines)))
    sentence_list = []
    transliter_list = []
    for sentence in lines:
        st = sentence.strip()
        tr = me(st)
        sentence_list.append(st)
        transliter_list.append(tr)

    data = pd.DataFrame({'Original Text': sentence_list, 'Transliterated Text': transliter_list}, index=index_list)
    data.to_csv("output_me.csv", encoding="utf-8-sig")
    print(data)
    f.close()

# Serbian
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