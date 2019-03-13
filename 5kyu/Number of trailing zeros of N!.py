"""
Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 * ... * N

Be careful 1000! has 2568 digits...
"""


def zeros(n):
	k = 1
	num = 0
	while pow(5, k) < n:
		num += n // pow(5, k)
		k += 1
	return num
