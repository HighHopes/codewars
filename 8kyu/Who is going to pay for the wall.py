"""Your code will show Full name of the neighbor and the truncated version of the name as an array. If the number of the characters in name is equal or less than two, it will return an array containing only the name as is"""

def who_is_paying(name):
    result = []
    if len(name) <= 2:
        return [name]
    else:
        result.append(name)
        result.append(name[0:2])

    return result


print(who_is_paying("Mexico"))  # ["Mexico", "Me"]
print(who_is_paying("Melania"))  # ["Melania", "Me"]
print(who_is_paying("Melissa"))  # ["Melissa", "Me"]
print(who_is_paying("Me"))  # ["Me"]
print(who_is_paying(""))  #  [""]
print(who_is_paying("I"))  #  ["I"]
