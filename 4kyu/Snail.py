"""Snail Sort
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]"""


def snail(snail_map):
    if len(snail_map) == 0:
        return snail_map

    result = []

    while snail_map:
        try:
            # add first row
            result.extend(snail_map[0])
            del snail_map[0]

            # add last element for every row
            for i in snail_map:
                result.append(i.pop(len(i)-1))

            # add last row
            result.extend(snail_map[-1][::-1])
            del snail_map[-1]

            # add first element of every row
            temp = []
            for i in snail_map:
                temp.append(i.pop(0))
            result.extend(temp[::-1])
        except IndexError:
            pass

    return result


b = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

print(snail(b))
