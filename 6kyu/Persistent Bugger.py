'''Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.
Example: persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2.'''


def persistence(n, c=1):
	if n < 10:
		return 0
	else:
		mul = 1
		for i in str(n):
			if int(i) == 0:
				mul *= 0
				break
			else:
				mul *= int(i)

		if mul < 10:
			return c
		else:
			return persistence(mul, c + 1)


print(persistence(39))  # 3
print(persistence(4))  # 0
print(persistence(25))  # 2
print(persistence(999))  # 4
print(persistence(23102))  # 1
