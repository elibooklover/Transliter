from TransLiter.ko_jamo import *

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