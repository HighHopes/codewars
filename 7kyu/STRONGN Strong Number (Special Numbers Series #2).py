"""Strong number is the number that the sum of the factorial of its digits is equal to number itself.

For example: 145, since
1! + 4! + 5! = 1 + 24 + 120 = 145
So, 145 is a Strong number."""

"""
import math

def strong_num(number):
    return "STRONG!!!!" if sum(math.factorial(int(i)) for i in str(number)) == number else "Not Strong !!"
"""


def factorial(number):
    result = 1
    for i in [i for i in range(1, number + 1)]:
        result *= i
    return result


def strong_num(number):
    return "STRONG!!!!" if sum(factorial(int(i)) for i in str(number)) == number else "Not Strong !!"


# print(strong_num(1))  # "STRONG!!!!"
# print(strong_num(2))  # "STRONG!!!!"
print(strong_num(145))  # "STRONG!!!!"

# print(strong_num(7))  # "Not Strong !!"
# print(strong_num(93))  # "Not Strong !!"
print(strong_num(185))  # "Not Strong !!"
