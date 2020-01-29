import re

def increment_string(strng):
    if strng == "": return 1
    if not strng[-1].isdigit(): return strng + "1"

    match = re.match(r"([a-z]+)([0-9]+)", strng, re.I)

    if match:
        strng = match.groups()

    strng = list(strng)

    strng[1] = str(int(strng[1]) + 1).zfill(len(strng[1]))

    return "".join(strng)


print(increment_string("foo"))  # "foo1"
print(increment_string("foobar0001"))  # "foobar002"
print(increment_string("foobar1"))  # "foobar2"
print(increment_string("foobar00"))  # "foobar01"
print(increment_string("foobar99"))  # "foobar100"
print(increment_string("foobar099"))  # "foobar100"
