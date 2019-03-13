"""Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true"""


def xo(s):
	x_count = 0
	o_count = 0

	for i in range(0, len(s)):
		if s[i].lower() == 'x':
			x_count += 1
		elif s[i].lower() == 'o':
			o_count += 1

	if x_count == 0 and o_count == 0:
		return True
	elif x_count == o_count:
		return True
	else:
		return False
