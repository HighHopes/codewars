"""Definition
Disarium number is the number that The sum of its digits powered with their respective positions is equal to the number itself.

Task
Given a number, Find if it is Disarium or not .

Notes
Number passed is always Positive .
Return the result as String
Input >> Output Examples
disariumNumber(89) ==> return "Disarium !!"
Explanation:
Since , 81 + 92 = 89 , thus output is "Disarium !!" """


def disarium_number(number):
    lst = list(map(int, str(number)))
    sum = 0

    for i, j in enumerate(lst):
        sum += pow(j, i+1)

    return "Disarium !!" if sum == number else "Not !!"


print(disarium_number(89))
print(disarium_number(564))
