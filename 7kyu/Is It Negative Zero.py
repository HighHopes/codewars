"""There exist two zeroes: +0 (or just 0) and -0.

Write a function that returns true if the input number is -0 and false otherwise (True and False for Python).

In JavaScript / TypeScript / Coffeescript the input will be a number.

In Python / Java / C / Haskell the input will be a float."""


def is_negative_zero(n):
	print(n)
	return True if n == 0 and str(n)[0] == "-" else False
