"""Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]"""


def unique_in_order(iterable):
	if type(iterable) is not int:
		a = list(iterable)
	else:
		a = list(map(int, str(iterable)))
	n = 0
	m = 1

	for i in a[:-1]:
		if a[n] == a[m]:
			a.pop(m)
		else:
			n += 1
			m += 1
	return a
