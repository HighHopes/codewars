"""Definition
Jumping number is the number that All adjacent digits in it differ by 1.

Task
Given a number, Find if it is Jumping or not .

Notes
Number passed is always Positive .

Return the result as String .

The difference between ‘9’ and ‘0’ is not considered as 1 .

All single digit numbers are considered as Jumping numbers."""


def jumping_number(number):
    lst = list(map(int, str(number)))

    for i in range(len(lst)-1):
        if abs(lst[i] - lst[i+1]) != 1:
            return "Not!!"

    return "Jumping!!"


print(jumping_number(898761))
