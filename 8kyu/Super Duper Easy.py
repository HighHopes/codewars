"""Make a function that returns the value multiplied by 50 and increased by 6. If the value entered is a string it should return "Error"."""

def problem(a):
    return a * 50 + 6 if type(a) == int or type(a) == float else "Error"


print(problem(1))
print(problem(1.5))
print(problem("asdf"))