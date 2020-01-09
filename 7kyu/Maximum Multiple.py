"""Task
Given a Divisor and a Bound , Find the largest integer N , Such That ,

Conditions :
N is divisible by divisor

N is less than or equal to bound

N is greater than 0.

Notes
The parameters (divisor, bound) passed to the function are only positve values .
It's guaranteed that a divisor is Found .
Input >> Output Examples
maxMultiple (2,7) ==> return (6)"""

def max_multiple(divisor, bound):
    while bound > 0:
        if bound % divisor == 0:
            return bound
        bound -= 1


print(max_multiple(2,7))  #6
print(max_multiple(3,10))  #9
print(max_multiple(7,17))  #14
print(max_multiple(10,50))  #50
print(max_multiple(37,200))  #185
print(max_multiple(7,100))  #98
