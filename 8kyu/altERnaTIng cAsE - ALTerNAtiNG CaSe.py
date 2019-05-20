"""Define String.prototype.toAlternatingCase (or a similar function/method such as to_alternating_case/toAlternatingCase/ToAlternatingCase in your selected language; see the initial solution for details) such that each lowercase letter becomes uppercase and each uppercase letter becomes lowercase. For example:

"hello world".toAlternatingCase() === "HELLO WORLD"
"HeLLo WoRLD".toAlternatingCase() === "hEllO wOrld"""


def to_alternating_case(string):
    return "".join(i.upper() if i.islower() else i.lower() for i in string)


print(to_alternating_case("hello WORLD"))  # "HELLO world"
print(to_alternating_case("HeLLo WoRLD"))  # "hEllO wOrld"
