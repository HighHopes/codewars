"""##Task: You have to write a function pattern which returns the following Pattern(See Pattern & Examples) upto n number of rows.

    Note:Returning the pattern is not the same as Printing the pattern.

####Rules/Note:

    If n < 1 then it should return "" i.e. empty string.
    There are no whitespaces in the pattern.

###Pattern:

1
22
333
....
.....
nnnnnn"""


def pattern(n):
    result = ""
    for i in range(0, n+1):
        result += str(i) * i + "\n"
    return result.strip("\n")