"""Create a function called shortcut to remove all the lowercase vowels in a given string.

Examples
shortcut("codewars") # --> cdwrs
shortcut("goodbye")  # --> gdby"""


def shortcut(s):
    r = ""
    for i in s:
        for j in i:
            if j not in "aeiou":
                r += j
    return r
