"""Modify the kebabize function so that it converts a camel case string into a kebab case.

kebabize('camelsHaveThreeHumps') // camels-have-three-humps
kebabize('camelsHave3Humps') // camels-have-humps"""


def kebabize(string):
	string = ''.join([i for i in string if not i.isdigit()])
	string = ''.join([i for i in string if i != '-'])

	new_string = ''
	for i in range(0, len(string)):
		if string[i].isupper():
			if i != 0:
				new_string += '-' + string[i].lower()
			else:
				new_string += string[i].lower()
		else:
			new_string += string[i].lower()

	return new_string


print(kebabize('SOSasdfasSADasda'))
print(kebabize('SOS'))
print(kebabize('23SOSssS'))
