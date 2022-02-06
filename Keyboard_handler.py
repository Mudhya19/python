# Keyboard handler
# https://www.codewars.com/kata/609d17f9838b2c0036b10e89/train/python

def handler(key, is_caps=False, is_shift=False):
    if not isinstance(key, str) or len(key) != 1 or key.isupper():
        return 'KeyError'

    num = "1234567890-=[];',./"
    unNum = '!@#$%^&*()_+{}:"<>?|'

    if key.isalpha() and (is_caps != is_shift):
        return key.upper()

    if not key.isalpha() and is_shift:
        return key.translate(str.maketrans(num, unNum))

    return key
