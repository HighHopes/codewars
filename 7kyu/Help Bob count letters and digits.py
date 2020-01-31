"""Bob is a lazy man.

He needs you to create a method that can determine how many letters and digits are in a given string.

example:

"hel2!lo" --> 6

"wicked .. !" --> 6"""


import re

def count_letters_and_digits(s):
    if s == None: return 0
    return len(re.findall("[a-zA-Z0-9]", str(s)))


print(count_letters_and_digits("asdf!@A#12sd"))  # 9
