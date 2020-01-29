"""Definition (Primorial Of a Number)
Is similar to factorial of a number, In primorial, not all the natural numbers get multiplied, only prime numbers are multiplied to calculate the primorial of a number. It's denoted with P#.

Task
Given a number N , calculate its primorial. !alt !alt

Notes
Only positive numbers will be passed (N > 0) .
Input >> Output Examples:
1- numPrimorial (3) ==> return (30)
Explanation:
Since the passed number is (3) ,Then the primorial should obtained by multiplying 2 * 3 * 5 = 30 .

Mathematically written as , P3# = 30 .
2- numPrimorial (5) ==> return (2310)
Explanation:
Since the passed number is (5) ,Then the primorial should obtained by multiplying 2 * 3 * 5 * 7 * 11 = 2310 .

Mathematically written as , P5# = 2310 ."""


import math

def is_prime(n):
    # True - prime. False - not prime

    # If it's even then it's not prime
    if n > 2 and n % 2 == 0:
        return False

    max_divisor = math.floor(math.sqrt(n))

    for i in range(3, max_divisor + 1, 2):
        if n % i == 0:
            return False

    return True

def num_primorial(n):
    prime_lst = [2]
    num = 3

    while len(prime_lst) < n:
        if is_prime(num):
            prime_lst.append(num)
        num += 2

    prod = 1

    for i in prime_lst:
        prod *= i
    return prod


print(num_primorial(68))
