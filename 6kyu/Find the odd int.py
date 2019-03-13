'''Given an array, find the int that appears an odd number of times. There will always be only one integer that appears an odd number of times.'''


def find_it(seq):
	return list(i for i in set(seq) if seq.count(i) % 2 != 0)


print(find_it([2, 2, 3, 3, 3]))
