
import numpy as np


def encrypt_cae(original_text, key):
    translated_text = ""
    for symbol in original_text:
        if symbol.isalpha():
            if symbol.isupper():
                symbol = chr(ord(symbol) + key)
                if symbol > 'Я':
                    symbol = chr(ord(symbol) - 32)
            else:
                symbol = chr(ord(symbol) + key)
                if symbol > 'я':
                    symbol = chr(ord(symbol) - 32)
        translated_text += symbol
    return translated_text


def decrypt_cae(original_text, key):
    return encrypt_cae(original_text, 32 - key)


def break_cae(original_text):
    letters = np.zeros(33)
    for symbol in original_text.lower():
        if symbol.isalpha():
            letters[ord(symbol) - ord('а')] += 1
    key = np.argmax(letters) - 14
    if key < 0:
        key += 32
    return decrypt_cae(original_text, key)
