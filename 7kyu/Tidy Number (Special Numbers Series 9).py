"""Definition
A Tidy number is a number whose digits are in non-decreasing order.

Task
Given a number, Find if it is Tidy or not .

Notes
Number passed is always Positive .

Return the result as a Boolean

Input >> Output Examples
tidyNumber (12) ==> return (true)
Explanation:
The number's digits { 1 , 2 } are in non-Decreasing Order (i.e) 1 <= 2 ."""


def tidyNumber(n):
    lst = [int(i) for i in str(n)]

    return lst == sorted(lst)


print(tidyNumber(12354))
