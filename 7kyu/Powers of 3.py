"""Given a positive integer N, return the largest integer k such that 3^k < N.

For example,

largestPower(3) = 0
largestPower(4) = 1
You may assume that the input to your function is always a positive integer."""


def largestPower(N):
    result = 0
    while 3 ** result < N:
        result += 1
    
    return result - 1


print(largestPower(3))  # 0
print(largestPower(4))  # 1
