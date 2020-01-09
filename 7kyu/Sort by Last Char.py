"""Given a string of words (x), you need to return an array of the words, sorted alphabetically by the final character in each.

If two words have the same last letter, they returned array should show them in the order they appeared in the given string.

All inputs will be valid."""

def last(x):
    return sorted(x.split(), key=lambda i: i[-1])

print(last("man i need a taxi up to ubud"))
