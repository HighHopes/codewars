"""Description:

#Task:

Write a function that returns true if the number is a "Very Even" number.

If the number is odd, it is not a "Very Even" number.

If the number is even, return whether the sum of the digits is a "Very Even" number.

#Examples:

input(88) => returns false -> 8 + 8 = 16 -> 1 + 6 = 7 => 7 is odd

input(222) => returns true

input(5) => returns false"""


def is_very_even_number(n):
    while True:
        n = sum(map(int, str(n)))
        if len(str(n)) == 1:
            return True if n % 2 == 0 else False


print(is_very_even_number(4))
