"""Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests."""


def first_non_repeating_letter(string):
    if len(string) == 0: return ''
    result = ''
    string_low = string.lower()
    for i in range(len(string_low)):
        if string_low.count(string_low[i]) == 1:
            result += string[i]
            break
    return result


print(first_non_repeating_letter('sTress'))  # T
