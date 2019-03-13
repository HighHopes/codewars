"""You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0."""


def expanded_form(num):
	if num < 10:
		return str(num)
	else:
		result = ''
		k = len(str(num)) - 1
		while k > 0:
			for i in str(num):
				if int(i) != 0:
					result += str(int(i) * pow(10, k)) + ' + '
					k -= 1
				else:
					k -= 1

	result = result.strip(' + ')
	return result


print(expanded_form(2))  # 2
print(expanded_form(703940))  # 700000 + 3000 + 900 + 40
print(expanded_form(342))  # 300 + 40 + 2
print(expanded_form(12))  # 10 + 2
print(expanded_form(20010))  # 20000 + 10
print(expanded_form(10))  # 0
