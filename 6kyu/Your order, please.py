'''Your task is to sort a given string. Each word in the string will contain a single number (from 1 to 9). This number is the position the word should have in the result. If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.
Examples: "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"'''


def order(sentence):
	words = sentence.split()

	l = [None] * len(words)
	for w in words:
		for i in w:
			if i.isdigit():
				i = int(i)
				l[i - 1] = w

	result = ''
	for i in l:
		result += i + ' '

	result = result.strip()
	return result


print(order("is2 Thi1s T4est 3a"))
