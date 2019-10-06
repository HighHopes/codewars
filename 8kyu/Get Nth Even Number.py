"""Return the Nth Even Number

nthEven(1) //=> 0, the first even number is 0
nthEven(3) //=> 4, the 3rd even number is 4 (0, 2, 4)

nthEven(100) //=> 198
nthEven(1298734) //=> 2597466"""


def nth_even(n):
    return n * 2 - 2


print(nth_even(1))
# print(nth_even(2))
# print(nth_even(3))
# print(nth_even(100))
# print(nth_even(1298734))
