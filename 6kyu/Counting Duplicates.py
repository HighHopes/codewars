"""Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times"""


def duplicate_count(text):
	counter = 0
	for i in list(set(text.lower())):
		if i in text.lower() and text.lower().count(i) > 1:
			counter += 1
	return counter


print(duplicate_count("indivisibility"))
