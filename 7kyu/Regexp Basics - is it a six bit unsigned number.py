"""Implement String#six_bit_number?, which should return true if given object is a number representable by 6 bit unsigned integer (0-63), false otherwise.

It should only accept numbers in canonical representation, so no leading +, extra 0s, spaces etc."""


def six_bit_number(n):
    return False if not n.isnumeric() or int(n) < 0 or int(n) > 63 or len(n) != len(str(int(n))) else True
