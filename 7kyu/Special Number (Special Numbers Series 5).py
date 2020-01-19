"""efinition
A number is a Special Number if it’s digits only consist 0, 1, 2, 3, 4 or 5

Given a number determine if it special number or not .

Notes
The number passed will be positive (N > 0) .

All single-digit numbers with in the interval [0:5] are considered as special number."""


def special_number(number):
    if "6" in set(str(number)): return "NOT!!"
    elif "7" in set(str(number)): return "NOT!!"
    elif "8" in set(str(number)): return "NOT!!"
    elif "9" in set(str(number)): return "NOT!!"
    else: return "Special!!"

print(special_number(123417))
