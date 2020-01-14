"""Given an array of 3 integers a, b and c, determine if they form a pythagorean triple.

Given an array of 3 integers a, b and c, determine if they form a pythagorean triple."""


def pythagorean_triple(integers):
    m = max(integers)
    integers.pop(integers.index(m))
    return pow(m, 2) == pow(integers[0], 2) + pow(integers[1], 2)


print(pythagorean_triple([3, 4, 5]))
print(pythagorean_triple([3, 9, 5]))
