"""Definition
A number is called Automorphic number if and only if its square ends in the same digits as the number itself.

Task
Given a number determine if it Automorphic or not .

Notes
The number passed to the function is positive

Single-digit numbers are considered Automorphic number.

Input >> Output Examples
autoMorphic (25) -->> return "Automorphic"
Explanation:
25 squared is 625 , Ends with the same number's digits which are 25 ."""


def automorphic(n):
    return "Automorphic" if n == int(str(pow(n, 2))[-len(str(n)):]) else "Not!!"


print(automorphic(9))
print(automorphic(5))
