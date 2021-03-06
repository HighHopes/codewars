"""In this example you have to validate if a user input string is alphanumeric. The given string is not nil, so you don't have to check that.

The string has the following conditions to be alphanumeric:

At least one character ("" is not valid)
Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
No whitespaces/underscore"""

import re


def alphanumeric(string):
    return len(re.findall("[^a-zA-Z0-9]", string)) == 0


print(alphanumeric("hello_world"))  # False
print(alphanumeric("PassW0rd"))  # True
