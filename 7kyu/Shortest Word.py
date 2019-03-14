"""Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types."""


def find_short(s):
	a = s.split()
	l = len(a[0])
	for i in a:
		if len(i) <= l:
			l = len(i)
	return l  # l: shortest word length
