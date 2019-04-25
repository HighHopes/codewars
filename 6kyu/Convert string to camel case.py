"""Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized.

Examples
to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"""

import re


def to_camel_case(text):
	words = re.split("[-_]", text)

	return words[0] + "".join([words[i].title() for i in range(1, len(words))])


print(to_camel_case("the_stealth_warrior"))
print(to_camel_case("The-stealth-warrior"))
