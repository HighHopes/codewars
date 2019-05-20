"""Given an array of strings, reverse them and their order in such way that their length stays the same as the length of the original inputs.

Example:
Input:  {"I", "like", "big", "butts", "and", "I", "cannot", "lie!"}
Output: {"!", "eilt", "onn", "acIdn", "ast", "t", "ubgibe", "kilI"}"""


def reverse(a):
    b = "".join(a)[::-1]
    c = []
    for i in a:
        c.append(b[0:len(i)])
        b = b[len(i)::]
    return c


print(reverse(["I", "like", "big", "butts", "and", "I", "cannot",
               "lie!"]))  # ["!", "eilt", "onn", "acIdn", "ast", "t", "ubgibe", "kilI"]
