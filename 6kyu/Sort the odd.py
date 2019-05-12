"""You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it."""


def sort_array(source_array):
	odd_sorted = sorted([i for i in source_array if i % 2 != 0])

	pos = 0
	result = []

	for i in source_array:
		if i % 2 != 0:
			result.append(odd_sorted[pos])
			pos += 1
		else:
			result.append(i)

	return result


print(sort_array([5, 3, 2, 8, 1, 4]))  # [1, 3, 2, 8, 5, 4]
print(sort_array([5, 3, 1, 8, 0]))  # [1, 3, 5, 8, 0]
print(sort_array([]))  # []
