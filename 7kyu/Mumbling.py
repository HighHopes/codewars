"""This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"""


def accum(s):
	result = ''
	for index, item in enumerate(s.lower()):
		result += item.upper() + item * int(index) + "-"
	return result[:-1]
