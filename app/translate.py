
from .cyphers import cypher_cae as CCae
from .cyphers import cypher_vig as CVig
from .cyphers import cypher_ver as CVer


def encrypt(original_text, cypher, key):
    
    try:
        is_cyrillic(original_text)
        is_cyrillic(key)
    except ValueError:
        return language_error_msg()
    except:
        return common_error_msg()
    
    if cypher == "cae":
        try:
            key_number = int(key)
            if key_number < 0 or key_number > 32:
                raise ValueError('Некорректный ключ')
            return CCae.encrypt_cae(original_text, key_number)
        except ValueError:
            return key_error_msg()
        except:
            return common_error_msg()
    
    elif cypher == "vig":
        try:
            for symbol in key:
                if not symbol.isalpha():
                    raise ValueError('Некорректный ключ')
            return CVig.encrypt_vig(original_text, key)
        except ValueError:
            return key_error_msg()
        except:
            return common_error_msg()
    
    else:
        try:
            for symbol in key:
                if not symbol.isalpha():
                    raise ValueError('Некорректный ключ')
            symbols_in_text = 0
            for symbol in original_text:
                if symbol.isalpha():
                    symbols_in_text += 1
            if len(key) < symbols_in_text:
                raise ValueError('Некорректный ключ')
            return CVer.encrypt_ver(original_text, key)
        except ValueError:
            return key_error_msg()
        except:
            return common_error_msg()


def decrypt(original_text, cypher, key):
    
    try:
        is_cyrillic(original_text)
        is_cyrillic(key)
    except ValueError:
        return language_error_msg()
    except:
        return common_error_msg()
    
    if cypher == "cae":
        try:
            key_number = int(key)
            if key_number < 0 or key_number > 32:
                raise ValueError('Некорректный ключ')
            return CCae.decrypt_cae(original_text, key_number)
        except ValueError:
            return CCae.break_cae(original_text)
        except:
            return common_error_msg()
    
    elif cypher == "vig":
        try:
            for symbol in key:
                if not symbol.isalpha():
                    raise ValueError('Некорректный ключ')
            return CVig.decrypt_vig(original_text, key)
        except ValueError:
            return key_error_msg()
        except:
            return common_error_msg()
    
    else:
        try:
            for symbol in key:
                if not symbol.isalpha():
                    raise ValueError('Некорректный ключ')
            symbols_in_text = 0
            for symbol in original_text:
                if symbol.isalpha():
                    symbols_in_text += 1
            if len(key) < symbols_in_text:
                raise ValueError('Некорректный ключ')
            return CVer.decrypt_ver(original_text, key)
        except ValueError:
            return key_error_msg()
        except:
            return common_error_msg()


def is_cyrillic(text):
    alphabet = {'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й',
                'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
                'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'}
    for symbol in text.lower():
        if symbol.isalpha():
            if symbol not in alphabet:
                raise ValueError('Некорректные символы')


def language_error_msg():
    language_error_msg = "ОШИБКА. Похоже, были введены символы не из русского алфавита."
    return language_error_msg


def key_error_msg():
    key_error_msg = "ОШИБКА. Для выбранного Вами шифра необходимо ввести корректный ключ."
    return key_error_msg


def common_error_msg():
    common_error_msg = "ОШИБКА. Что-то пошло не так."
    return common_error_msg
