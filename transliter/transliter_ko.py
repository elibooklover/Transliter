from transliter.ko_jamo import *
import re
import pandas as pd
import os

def convert(Ko_words):
    split_word_list = list(Ko_words)
    jamo_result = []
    for keyword in split_word_list:
        if re.match('.*[가-힣]+.*', keyword):
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
    letter = list(text)
    transliterated_letters = []
    for i in range(len(letter)-1):
        transliterated_letter = ''
        try:
            if letter[i] in JONGSUNG_LIST2 and letter[i+1] in CHOSUNG_LIST2:
                transliterated_letter += JONGSUNG_ALPHABET[letter[i]]
            elif letter[i] in CHOSUNG_LIST or JUNGSUNG_LIST:
                transliterated_letter += KOREAN_ALPHABET[letter[i]]
            else:
                transliterated_letter += letter[i]
            transliterated_letters.append(transliterated_letter)
        except KeyError:
            transliterated_letter += letter[i]
            transliterated_letters.append(transliterated_letter)
    if len(letter) > 1:
        if letter[-1] in JONGSUNG_LIST2:
            transliterated_letters.append(JONGSUNG_ALPHABET[letter[-1]])
        elif letter[-1] in JUNGSUNG_LIST:
            transliterated_letters.append(KOREAN_ALPHABET[letter[-1]])
        else:
            transliterated_letters.append(letter[-1])
    transliterated_word = ''.join(transliterated_letters)
    return transliterated_word
