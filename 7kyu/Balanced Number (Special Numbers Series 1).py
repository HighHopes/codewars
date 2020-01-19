"""Definition
Balanced number is the number that * The sum of all digits to the left of the middle digit(s) and the sum of all digits to the right of the middle digit(s) are equal*.

Task
Given a number, Find if it is Balanced or not .

Notes
If the number has an odd number of digits then there is only one middle digit, e.g. 92645 has middle digit 6; otherwise, there are two middle digits , e.g. 1301 has middle digits 3 and 0

The middle digit(s) should not be considered when determining whether a number is balanced or not, e.g 413023 is a balanced number because the left sum and right sum are both 5.

Number passed is always Positive .

Return the result as String

Input >> Output Examples
balancedNum (7) ==> return "Balanced"
Explanation:
Since , The sum of all digits to the left of the middle digit (0)

and the sum of all digits to the right of the middle digit (0) are equal , then It's Balanced"""


def balanced_num(number):
    half = len(str(number)) // 2

    if len(str(number)) % 2 != 0:
        return "Balanced" if sum(map(int, str(number)[0:half])) == sum(map(int, str(number)[half+1::])) else "Not Balanced"
    else:
        return "Balanced" if sum(map(int, str(number)[0:half-1])) == sum(map(int, str(number)[half+1::])) else "Not Balanced"


print(balanced_num(7)  )  # "Balanced"
print(balanced_num(959))  # "Balanced"
print(balanced_num(123404321))  # "Balanced"
print(balanced_num(1234002321))  # "Balanced"
print(balanced_num(13) )  # "Balanced"
print(balanced_num(432))  # "Not Balanced"
print(balanced_num(424))  # "Balanced"
