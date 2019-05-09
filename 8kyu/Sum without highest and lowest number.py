"""Sum all the numbers of the array (in F# and Haskell you get a list) except the highest and the lowest element (the value, not the index!).
(The highest/lowest element is respectively only one element at each edge, even if there are more than one with the same value!)"""


def sum_array(arr):
	if arr is not None:
		if len(arr) > 2:
			return sum(arr) - max(arr) - min(arr)
		else:
			return 0
	else:
		return 0


print(sum_array(None))
