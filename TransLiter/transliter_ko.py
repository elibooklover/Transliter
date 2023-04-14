from TransLiter.ko_jamo import *
import re
import pandas as pd

def convert(Ko_words):
    split_word_list = list(Ko_words)
    jamo_result = []
    for keyword in split_word_list:
        if re.match('.*[가-힣]+.*', keyword) is not None:
            char_code = ord(keyword) - BASE_CODE
            char1 = int(char_code / CHOSUNG)
            char2 = int((char_code - (CHOSUNG * char1)) / JUNGSUNG)
            jamo_result.append(CHOSUNG_LIST[char1])
            jamo_result.append(JUNGSUNG_LIST[char2])
            char3 = int((char_code - (CHOSUNG * char1) - (JUNGSUNG * char2)))
            if char3==0:
                jamo_result.append('')
            else:
                jamo_result.append(JONGSUNG_LIST[char3])
        else:
            jamo_result.append(keyword)
    return "".join(jamo_result)

def ko(text):
    text = convert(text)
    syllables = list(text)
    transliterated_syllables = []
    for syllable in syllables:
        transliterated_syllable = ''
        for letter in syllable:
            if letter in KOREAN_ALPHABET:
                transliterated_syllable += KOREAN_ALPHABET[letter]
            else:
                transliterated_syllable += letter
        transliterated_syllables.append(transliterated_syllable)
    transliterated_word = ''.join(transliterated_syllables)
    return transliterated_word

def transliter_ko():
    while True:
        input_text = input("Please enter Korean text: ")
        print(ko(input_text))
        if input_text == "": 
            break

def txt_ko(file):
    f = open(file, 'r')
    f2 = open("output_ko.txt", 'w')
    result = ""
    while True:
        line = f.readline()
        result += line + ko(line)
        if not line: 
            break
    print(result)
    f2.write(result)
    f.close()
    f2.close()

def csv_ko(file):
    data = pd.DataFrame(columns=['Original Text', 'Transliterated Text'])
    f = open(file, 'r')
    lines = f.readlines()
    
    index_list = list(range(len(lines)))
    sentence_list = []
    transliter_list = []
    for sentence in lines:
        st = sentence.strip()
        tr = ko(st)
        sentence_list.append(st)
        transliter_list.append(tr)

    data = pd.DataFrame({'Original Text': sentence_list, 'Transliterated Text': transliter_list}, index=index_list)
    data.to_csv("output_ko.csv", encoding="utf-8-sig")
    print(data)
    f.close()