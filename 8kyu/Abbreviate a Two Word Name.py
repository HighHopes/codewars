"""Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot seperating them.

It should look like this:

Sam Harris => S.H

Patrick Feeney => P.F"""


def abbrevName(name):
	name = name.split()
	res = ""
	for i in name:
		res += i[0].upper()
		res += " "
	res = res.strip()
	res = res.replace(" ", ".")
	return res
