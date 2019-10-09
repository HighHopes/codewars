"""This kata is about multiplying a given number by eight if it is an even number and by nine otherwise."""


def simple_multiplication(number):
    return number * 9 if number % 2 != 0 else number * 8


print(simple_multiplication(2))
