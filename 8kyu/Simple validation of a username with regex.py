"""Write a simple regex to validate a username. Allowed characters are:

lowercase letters,
numbers,
underscore
Length should be between 4 and 16 characters (both included)."""

import re


def validate_usr(username):
	if len(username) < 4 or len(username) > 16:
		return False
	else:
		uname = re.sub("[a-z0-9_]", "", username)
		if len(uname) == 0:
			return True
		else:
			return False


print(validate_usr("alin"))
