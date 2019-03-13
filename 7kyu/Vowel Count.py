'''Return the number (count) of vowels in the given string. We will consider a, e, i, o, and u as vowels for this Kata. The input string will only consist of lower case letters and/or spaces.'''


def vowels(w):
	num_vowels = 0
	l = list(w)
	all_vowels = ['a', 'e', 'i', 'o', 'u']
	for i in l:
		if i.lower() in all_vowels:
			num_vowels += 1
	return num_vowels


print(vowels('asqwegsvczxqtghnuy'))
print(vowels('asjldbfavitdsgvacoblc'))
print(vowels('zxljhuiagfvobpasvugyoaveftqwysdbcnjbhsgfaivy'))
print(vowels('alsudhflaskjdlzxcvxbcmvbquiweyupiqwpeufiasdffhasdf'))
