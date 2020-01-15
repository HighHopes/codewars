"""Your task is to calculate logical value of boolean array. Test arrays are one-dimensional and their size is in the range 1-50.

Links referring to logical operations: AND, OR and XOR.

You should begin at the first value, and repeatedly apply the logical operation across the remaining elements in the array sequentially.

First Example:

Input: true, true, false, operator: AND

Steps: true AND true -> true, true AND false -> false

Output: false

Second Example:

Input: true, true, false, operator: OR

Steps: true OR true -> true, true OR false -> true

Output: true"""


def logical_calc(array, op):
    if op == "XOR": op = "^"
    s = op.lower().join([" " + str(i) + " " for i in array]).strip()

    return eval(s)
