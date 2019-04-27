"""Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string."""

import re


def fake_bin(x):
	x = re.sub("[1-4]", "0", x)
	x = re.sub("[5-9]", "1", x)

	return x


print(fake_bin("45385593107843568"))
