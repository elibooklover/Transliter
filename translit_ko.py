from ko_jamo import *

def translit_ko(text):
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

while True:
    input_text = input("Please enter Korean text: ")
    input_jamo = convert(input_text)
    print(translit_ko(input_jamo))