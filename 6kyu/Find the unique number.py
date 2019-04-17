"""There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains more than 3 numbers.

The tests contain some very huge arrays, so think about performance."""


def find_uniq(arr):
    if arr.count(arr[0]) > 1:
        dup = arr[0]
    else:
        return arr[0]

    return [i for i in list(set(arr)) if i != dup][0]


print(find_uniq([0, 0, 0.55, 0, 0]))
