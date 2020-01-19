"""Definition
Strong number is the number that the sum of the factorial of its digits is equal to number itself.

For example: 145, since
1! + 4! + 5! = 1 + 24 + 120 = 145
So, 145 is a Strong number.

Task
Given a number, Find if it is Strong or not.

Warm-up (Highly recommended)
Playing With Numbers Series
Notes
Number passed is always Positive.
Return the result as String
"""

def strong_num(number):
    lst = list(map(int, str(number)))

    result = []

    for i in range(len(lst)):
        fact = 1
        for j in range(1, lst[i]+1):
            fact = fact*j

        result.append(fact)

    return "STRONG!!!!" if sum(result) == number else "Not Strong !!"


print(strong_num(145))
