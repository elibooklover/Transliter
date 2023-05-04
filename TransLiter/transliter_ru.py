from TransLiter.ru_list import *

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

def transliter_ru():
    while True:
        input_text = input("Please enter Russian text: ")
        print(ru(input_text))
        if input_text == "": 
            break