"""Find the number with the most digits.

If two numbers in the argument array have the same number of digits, return the first one in the array."""


def find_longest(arr):
    h = arr[0]

    for i in arr:
        if len(str(i)) > len(str(h)):
            h = i

    return h


print(find_longest([1, 10, 100]))  # 100
print(find_longest([9000, 8, 800]))  # 9000
print(find_longest([8, 900, 500]))  # 900
print(find_longest([3, 40000, 100]))  # 40000
print(find_longest([1, 200, 100000]))  # 100000
