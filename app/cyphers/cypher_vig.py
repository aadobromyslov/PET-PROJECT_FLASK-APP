
import numpy as np


def encrypt_vig(original_text, key_word):
    translated_text = ""
    key = np.array([(ord(i) - ord('а')) for i in key_word.lower()])
    shift_idx = 0
    for symbol in original_text:
        if symbol.isalpha():
            if symbol.isupper():
                symbol = chr(ord(symbol) + key[shift_idx])
                if symbol > 'Я':
                    symbol = chr(ord(symbol) - 32)
            else:
                symbol = chr(ord(symbol) + key[shift_idx])
                if symbol > 'я':
                    symbol = chr(ord(symbol) - 32)
            shift_idx = (shift_idx + 1) % key.size
        translated_text += symbol
    return translated_text


def decrypt_vig(original_text, key_word):
    decrypt_word = ""
    for symbol in key_word.lower():
        decrypt_word += chr(ord('а') + 32 - (ord(symbol) - ord('а')))
    return encrypt_vig(original_text, decrypt_word)
