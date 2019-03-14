"""Count the number of occurrences of each character and return it as a list of tuples in order of appearance.

Example:

ordered_count("abracadabra") == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]"""


def ordered_count(input):
	no_dup = []
	for i in input:
		if i not in no_dup:
			no_dup.append(i)

	res = []
	for i in no_dup:
		temp = []
		temp.append(i)
		temp.append(input.count(i))
		res.append(tuple(temp))
	return res
