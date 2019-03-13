"""Write a simple parser that will parse and run Deadfish.

Deadfish has 4 commands, each 1 character long:

i increments the value (initially 0)
d decrements the value
s squares the value
o outputs the value into the return array
Invalid characters should be ignored.

parse("iiisdoso")  ==>  [8, 64]"""


def parse(data):
	lst = []

	k = 0
	for item in data:
		if item == "i":
			k += 1
		elif item == "s":
			k = pow(k, 2)
		elif item == "d":
			k -= 1
		elif item == "o":
			lst.append(k)

	return lst
