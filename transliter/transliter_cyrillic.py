from transliter.cyrillic_list import *
import pandas as pd
import os

# Russian
def ru(text):
    transliterated_text = ""
    for letter in text:
        try: 
            if letter in RUSSIAN_LIST:
                transliterated_text += RUSSIAN_LIST[letter]
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

def txt_ru(file):
    f = open(file, 'r')
    new_file = os.path.splitext(file)[0]
    f2 = open(f"{new_file}_output.txt", 'w')
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

def csv_ru(file):
    data = pd.DataFrame(columns=['Original Text', 'Transliterated Text'])
    f = open(file, 'r')
    new_file = os.path.splitext(file)[0]
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
    data.to_csv(f"{new_file}_output.csv", encoding="utf-8-sig")
    print(data)
    f.close()

# Ukrainian
def ua(text):
    transliterated_text = ""
    for letter in text:
        try:
            if letter in UKRAINIAN_LIST:
                transliterated_text += UKRAINIAN_LIST[letter]
            else:
                transliterated_text += letter
        except KeyError:
            pass
    return transliterated_text

def transliter_ua():
    while True:
        input_text = input("Please enter Ukrainian text: ")
        print(ua(input_text))
        if input_text == "": 
            break

def txt_ua(file):
    f = open(file, 'r')
    new_file = os.path.splitext(file)[0]
    f2 = open(f"{new_file}_output.txt", 'w')
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

def csv_ua(file):
    data = pd.DataFrame(columns=['Original Text', 'Transliterated Text'])
    f = open(file, 'r')
    new_file = os.path.splitext(file)[0]
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
    data.to_csv(f"{new_file}_output.csv", encoding="utf-8-sig")
    print(data)
    f.close()

# Bulgarian
def bg(text):
    transliterated_text = ""
    for letter in text:
        try: 
            if letter in BULGARIAN_LIST:
                transliterated_text += BULGARIAN_LIST[letter]
            else:
                transliterated_text += letter
        except KeyError:
            pass
    return transliterated_text

def transliter_bg():
    while True:
        input_text = input("Please enter Bulgarian text: ")
        print(bg(input_text))
        if input_text == "": 
            break

def txt_bg(file):
    f = open(file, 'r')
    new_file = os.path.splitext(file)[0]
    f2 = open(f"{new_file}_output.txt", 'w')
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

def csv_bg(file):
    data = pd.DataFrame(columns=['Original Text', 'Transliterated Text'])
    f = open(file, 'r')
    new_file = os.path.splitext(file)[0]
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
    data.to_csv(f"{new_file}_output.csv", encoding="utf-8-sig")
    print(data)
    f.close()

# Macedonian
def mk(text):
    transliterated_text = ""
    for letter in text:
        try: 
            if letter in MACEDONIAN_LIST:
                transliterated_text += MACEDONIAN_LIST[letter]
            else:
                transliterated_text += letter
        except KeyError:
            pass
    return transliterated_text

def transliter_mk():
    while True:
        input_text = input("Please enter Macedonian text: ")
        print(mk(input_text))
        if input_text == "": 
            break

def txt_mk(file):
    f = open(file, 'r')
    new_file = os.path.splitext(file)[0]
    f2 = open(f"{new_file}_output.txt", 'w')
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

def csv_mk(file):
    data = pd.DataFrame(columns=['Original Text', 'Transliterated Text'])
    f = open(file, 'r')
    new_file = os.path.splitext(file)[0]
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
    data.to_csv(f"{new_file}_output.csv", encoding="utf-8-sig")
    print(data)
    f.close()

# Mongolian
def mn(text):
    transliterated_text = ""
    for letter in text:
        try: 
            if letter in MONGOLIAN_LIST:
                transliterated_text += MONGOLIAN_LIST[letter]
            else:
                transliterated_text += letter
        except KeyError:
            pass
    return transliterated_text

def transliter_mn():
    while True:
        input_text = input("Please enter Mongolian text: ")
        print(me(input_text))
        if input_text == "": 
            break

def txt_mn(file):
    f = open(file, 'r')
    new_file = os.path.splitext(file)[0]
    f2 = open(f"{new_file}_output.txt", 'w')
    result = ""
    while True:
        line = f.readline()
        result += line + mn(line)
        if not line: 
            break
    print(result)
    f2.write(result)
    f.close()
    f2.close()

def csv_mn(file):
    data = pd.DataFrame(columns=['Original Text', 'Transliterated Text'])
    f = open(file, 'r')
    new_file = os.path.splitext(file)[0]
    lines = f.readlines()
    
    index_list = list(range(len(lines)))
    sentence_list = []
    transliter_list = []
    for sentence in lines:
        st = sentence.strip()
        tr = mn(st)
        sentence_list.append(st)
        transliter_list.append(tr)

    data = pd.DataFrame({'Original Text': sentence_list, 'Transliterated Text': transliter_list}, index=index_list)
    data.to_csv(f"{new_file}_output.csv", encoding="utf-8-sig")
    print(data)
    f.close()


# Montenegrin
def me(text):
    transliterated_text = ""
    for letter in text:
        try: 
            if letter in MONTENEGRIN_LIST:
                transliterated_text += MONTENEGRIN_LIST[letter]
            else:
                transliterated_text += letter
        except KeyError:
            pass
    return transliterated_text

def transliter_me():
    while True:
        input_text = input("Please enter Montenegrin text: ")
        print(me(input_text))
        if input_text == "": 
            break

def txt_me(file):
    f = open(file, 'r')
    new_file = os.path.splitext(file)[0]
    f2 = open(f"{new_file}_output.txt", 'w')
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

def csv_me(file):
    data = pd.DataFrame(columns=['Original Text', 'Transliterated Text'])
    f = open(file, 'r')
    new_file = os.path.splitext(file)[0]
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
    data.to_csv(f"{new_file}_output.csv", encoding="utf-8-sig")
    print(data)
    f.close()

# Serbian
def sr(text):
    transliterated_text = ""
    for letter in text:
        try: 
            if letter in SERBIAN_LIST:
                transliterated_text += SERBIAN_LIST[letter]
            else:
                transliterated_text += letter
        except KeyError:
            pass
    return transliterated_text

def transliter_sr():
    while True:
        input_text = input("Please enter Serbian text: ")
        print(sr(input_text))
        if input_text == "": 
            break

def txt_sr(file):
    f = open(file, 'r')
    new_file = os.path.splitext(file)[0]
    f2 = open(f"{new_file}_output.txt", 'w')
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

def csv_sr(file):
    data = pd.DataFrame(columns=['Original Text', 'Transliterated Text'])
    f = open(file, 'r')
    new_file = os.path.splitext(file)[0]
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
    data.to_csv(f"{new_file}_output.csv", encoding="utf-8-sig")
    print(data)
    f.close()

# Tajiki
def tj(text):
    transliterated_text = ""
    for letter in text:
        try: 
            if letter in TAJIKI_LIST:
                transliterated_text += TAJIKI_LIST[letter]
            else:
                transliterated_text += letter
        except KeyError:
            pass
    return transliterated_text

def transliter_tj():
    while True:
        input_text = input("Please enter Tajiki text: ")
        print(tj(input_text))
        if input_text == "": 
            break

def txt_tj(file):
    f = open(file, 'r')
    new_file = os.path.splitext(file)[0]
    f2 = open(f"{new_file}_output.txt", 'w')
    result = ""
    while True:
        line = f.readline()
        result += line + tj(line)
        if not line: 
            break
    print(result)
    f2.write(result)
    f.close()
    f2.close()

def csv_tj(file):
    data = pd.DataFrame(columns=['Original Text', 'Transliterated Text'])
    f = open(file, 'r')
    new_file = os.path.splitext(file)[0]
    lines = f.readlines()
    
    index_list = list(range(len(lines)))
    sentence_list = []
    transliter_list = []
    for sentence in lines:
        st = sentence.strip()
        tr = tj(st)
        sentence_list.append(st)
        transliter_list.append(tr)

    data = pd.DataFrame({'Original Text': sentence_list, 'Transliterated Text': transliter_list}, index=index_list)
    data.to_csv(f"{new_file}_output.csv", encoding="utf-8-sig")
    print(data)
    f.close()