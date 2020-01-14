"""Numbers ending with zeros are boring.

They might be fun in your world, but not here.

Get rid of them. Only the ending ones."""


def no_boring_zeros(n):
    if n == 0: return n
    return int(str(n).strip("0"))


print(no_boring_zeros(121200123400))
