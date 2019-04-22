"""We want to generate a function that computes the series starting from 0 and ending until the given number following the sequence:

0 1 3 6 10 15 21 28 36 45 55 ....

which is created by

0, 0+1, 0+1+2, 0+1+2+3, 0+1+2+3+4, 0+1+2+3+4+5, 0+1+2+3+4+5+6, 0+1+2+3+4+5+6+7 etc..

Input:

LastNumber

Output:

series and result"""


def show_sequence(n):
	result = ""
	if n == 0:
		return "0=0"
	elif n < 0:
		return "{}<0".format(n)
	else:
		for i in range(n + 1):
			result += str(i) + "+"
		result = result.strip("+")
		result += " = " + str(sum(i for i in range(n + 1)))
		return result
