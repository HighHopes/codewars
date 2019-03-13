"""Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''"""


def namelist(names):
	list_names = []

	if len(names) > 0:
		for i in names:
			list_names.append(i['name'])
	else:
		return ''

	result = ''
	for i in range(0, len(list_names)):
		if i >= len(list_names) - 2:
			result += list_names[i] + ' & '
		else:
			result += list_names[i] + ', '
	result = result.strip(' & ')

	return result


print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'},
				{'name': 'Marge'}]))  # 'Bart, Lisa, Maggie, Homer & Marge', "Must work with many names"
print(namelist(
	[{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))  # 'Bart, Lisa & Maggie', "Must work with many names"
print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}]))  # 'Bart & Lisa', "Must work with two names"
print(namelist([{'name': 'Bart'}]))  # 'Bart', "Wrong output for a single name"
print(namelist([]))  # '', "Must work with no names"
