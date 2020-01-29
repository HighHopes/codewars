"""Implement the function which should return true if given object is a vowel, false otherwise."""

import re

def is_vowel(s):
    if re.match(r"[aeiouAEIOU]", s) and len(s) == 1:
        return True
    else:
        return False


print(is_vowel(""))  # False
print(is_vowel("a"))  # True
print(is_vowel("E"))  # True
print(is_vowel("ou"))  # False
print(is_vowel("z"))  # False
print(is_vowel("lol"))  # False
