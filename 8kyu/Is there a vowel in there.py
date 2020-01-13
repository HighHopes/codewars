"""Given an array of numbers, check if any of the numbers are the character codes for lower case vowels (a, e, i, o, u).

If they are, change the array value to a string of that vowel.

Return the resulting array."""


def is_vow(inp):
    vowels = ["a", "e", "i", "o", "u"]
    result = []

    for i in inp:
        if chr(i) in vowels:
            result.append(chr(i))
        else:
            result.append(i)

    return result


print(is_vow([118,117,120,121,117,98,122,97,120,106,104,116,113,114,113,120,106 ]))
