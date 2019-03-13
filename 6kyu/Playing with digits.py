'''Given a positive integer n (n>0) written as abcd...x (a, b, c, d...x being digits) and a positive integer p (p>0) we want to find a positive integer k, if it exists (if not return -1), such as the sum of the digits of n taken to the successive powers of p is equal to k * n. In other words:

Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
Ex: n = 46288, p = 3 : 4^3 + 6^4+ 2^5 + 8^6 + 8^7 = 2360688 = 46288 * 51'''


def dig_pow(n, p):
	nList = [int(i) for i in str(n)]

	result = 0
	for i in nList:
		result += i ** p
		p += 1

	if result % n == 0:
		return int(result / n)
	else:
		return -1


print(dig_pow(46288, 3))
