"""Complete the function power_of_two/powerOfTwo (or equivalent, depending on your language) that determines if a given non-negative integer is a power of two. From the corresponding Wikipedia entry:

a power of two is a number of the form 2n where n is an integer, i.e. the result of exponentiation with number two as the base and integer n as the exponent.

You may assume the input is always valid.

Examples
power_of_two(1024) ==> True
power_of_two(4096) ==> True
power_of_two(333)  ==> False"""


def power_of_two(x):
	if x == 0:
		return False
	elif x == 1:
		return True
	elif x == 2:
		return True
	else:
		num = 2
		while num < x:
			num *= 2
		return num == x
