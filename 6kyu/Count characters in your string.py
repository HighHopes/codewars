"""The main idea is to count all the occuring characters(UTF-8) in string. If you have string like this aba then the result should be { 'a': 2, 'b': 1 }

What if the string is empty ? Then the result should be empty object literal { }"""


def count(string):
	result = {}
	for i in string:
		if i not in result.keys():
			result[i] = 1
		else:
			result[i] += 1
	return result


print(count("aba"))
