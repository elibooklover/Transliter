from transliter.cyrillic_list import *
import pandas as pd
import os

class TransliterCyrillic:
    def __init__(self, language_list):
        self.language_list = language_list

    def cyrillic(self, text):
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

def ru(text):
    transliterator = TransliterCyrillic(RUSSIAN_LIST)
    return transliterator.cyrillic(text)

def ua(text):
    transliter = TransliterCyrillic(UKRAINIAN_LIST)
    return transliter.cyrillic(text)

def bg(text):
    transliter = TransliterCyrillic(BULGARIAN_LIST)
    return transliter.cyrillic(text)

def mk(text):
    transliter = TransliterCyrillic(MACEDONIAN_LIST)
    return transliter.cyrillic(text)

def mn(text):
    transliter = TransliterCyrillic(MONGOLIAN_LIST)
    return transliter.cyrillic(text)

def me(text):
    transliter = TransliterCyrillic(MONTENEGRIN_LIST)
    return transliter.cyrillic(text)

def sr(text):
    transliter = TransliterCyrillic(SERBIAN_LIST)
    return transliter.cyrillic(text)

def tj(text):
    transliter = TransliterCyrillic(TAJIKI_LIST)
    return transliter.cyrillic(text)
