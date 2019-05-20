"""Your goal is to return multiplication table for number that is always an integer from 1 to 10.
For example, a multiplication table (string) for number == 5 looks like below:
P. S. You can use \n in string to jump to the next line."""


def multi_table(number):
    return "\n".join(str(i) + " * " + str(number) + " = " + str(i * number) for i in range(1, 11))


print(multi_table(5))
