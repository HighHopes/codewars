"""Remove a exclamation mark from the end of string. For a beginner kata, you can assume that the input data is always a string, no need to verify it."""


def remove(s):
	if len(s) > 0:
		return s[0:-1] if s[-1] == "!" else s
	else:
		return ""
