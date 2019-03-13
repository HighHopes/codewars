"""Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.

Input to the function is guaranteed to be a single string.

Examples
Valid inputs:

1.2.3.4
123.45.67.89
Invalid inputs:

1.2.3
1.2.3.4.5
123.456.78.90"""


def is_valid_IP(strng):
	if len(strng) == 0:
		return False
	else:
		strng = strng.split(".")
		if len(strng) != 4:
			return False
		else:
			for i in strng:
				if i.isalpha():
					return False
				elif not 0 <= int(i) <= 255:
					return False
				elif " " in i:
					return False
				elif len(i) > 1 and int(i[0]) < 1:
					return False

			return True
