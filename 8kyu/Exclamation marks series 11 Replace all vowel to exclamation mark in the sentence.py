"""Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.

Examples
replace("Hi!") === "H!!"
replace("!Hi! Hi!") === "!H!! H!!"
replace("aeiou") === "!!!!!"
replace("ABCDE") === "!BCD!"""

import re


def replace_exclamation(s):
    return re.sub("[aeiouAEIOU]", "!", s)


print(replace_exclamation("Hie!"))
