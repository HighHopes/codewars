"""Given a List [] of n integers , find minimum mumber to be inserted in a list, so that sum of all elements of list should equal the closest prime number .

Notes
List size is at least 2 .

List's numbers will only positives (n > 0) .

Repeatition of numbers in the list could occur .

The newer list's sum should equal the closest prime number .

Input >> Output Examples
1- minimumNumber ({3,1,2}) ==> return (1)
Explanation:
Since , the sum of the list's elements equal to (6) , the minimum number to be inserted to transform the sum to prime number is (1) , which will make *the sum of the List** equal the closest prime number (7)* ."""

import math

def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(math.sqrt(n) + 1), 6):
        if n % i == 0 or n % (i+2) == 0:
            return False

    return True

def nextPrime(n):
    if n <= 1:
        return 2

    prime = n
    found = False

    while(not found):
        prime += 1
        if isPrime(prime) == True:
            found = True

    return prime

def minimum_number(numbers):
    sum_of_lst = sum(numbers)

    if isPrime(sum_of_lst):
        return 0
    else:
        next_prime = nextPrime(sum_of_lst)
        result = next_prime - sum_of_lst

        return result


print(minimum_number([5,2]))
