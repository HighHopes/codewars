"""Your task is simply to count the total number of lowercase letters in a string.

Examples
lowercaseCount("abc"); ===> 3

lowercaseCount("abcABC123"); ===> 3"""


def lowercase_count(strng):
    c = 0
    for i in strng:
        if i in "abcdefghijklmnopqrstuvwxyz":
            c += 1
    return c
