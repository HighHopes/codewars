"""Given an integer as input, can you round it to the next (meaning, "higher") 5?

Examples:

input:    output:
0    ->   0
2    ->   5
3    ->   5

Input may be any positive or negative integer (including 0).

You can assume that all inputs are valid integers."""


def round_to_next5(n):
	for i in range(n, n + 6):
		if i % 5 == 0:
			return i
