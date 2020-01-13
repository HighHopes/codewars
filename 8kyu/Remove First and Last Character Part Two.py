"""This is a spin off of my first kata. You are given a list of character sequences as a comma separated string. Write a function which returns another string containing all the character sequences except the first and the last ones. If the input string is empty, or the removal of the first and last items would cause the string to be empty, return a null value."""


def array(string):
    r = " ".join(string.split(",")[1:-1])
    return None if r == "" else r


print(array("1, 2,3"))
print(array("1, 2,3, as,  asdf"))
print(array("12"))
