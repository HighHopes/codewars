"""A string is considered to be in title case if each word in the string is either (a) capitalised (that is, only the first letter of the word is in upper case) or (b) considered to be an exception and put entirely into lower case unless it is the first word, which is always capitalised.

Write a function that will convert a string into title case, given an optional list of exceptions (minor words). The list of minor words will be given as a string with each word separated by a space. Your function should ignore the case of the minor words string -- it should behave in the same way even if the case of the minor word string is changed.

title_case('a clash of KINGS', 'a an the of') # should return: 'A Clash of Kings'
title_case('THE WIND IN THE WILLOWS', 'The In') # should return: 'The Wind in the Willows'
"""


def title_case(title, minor_words=''):
	title = title.split()
	minor_words = minor_words.lower().split()
	new_title = []

	for i in range(0, len(title)):
		if i == 0:
			new_title.append(title[i].capitalize())
		elif i > 0:
			if title[i].lower() not in minor_words:
				new_title.append(title[i].capitalize())
			else:
				new_title.append(title[i].lower())
	title = ' '.join(new_title)
	return title


print(title_case('a clash of KINGS', 'a an the of'))  # should return: 'A Clash of Kings'
print(title_case('THE WIND IN THE WILLOWS', 'The In'))  # should return: 'The Wind in the Willows'
print(title_case('the quick brown fox'))  # should return: 'The Quick Brown Fox'
