"""	In this simple Kata your task is to create a function that turns a string into a Mexican Wave. You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up.
Rules
 	1.  The input string will always be lower case but maybe empty.

2.  If the character in the string is whitespace then pass over it as if it was an empty seat.
Example
wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]"""


def wave(str):
	result = []
	i = 0

	while i < len(str):
		if str[i] != " ":
			up = str[i].upper()
			new = str[0:i] + up + str[i + 1:]
			result.append(new)
		i += 1

	return result


print(wave("hello"))  # => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
print(wave(" gap "))  # => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
