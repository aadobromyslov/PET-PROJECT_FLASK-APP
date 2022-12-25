
from .cypher_vig import encrypt_vig
from .cypher_vig import decrypt_vig


def encrypt_ver(original_text, key_word):
    return encrypt_vig(original_text, key_word)
    
def decrypt_ver(original_text):
    return decrypt_vig(original_text, key_word)
