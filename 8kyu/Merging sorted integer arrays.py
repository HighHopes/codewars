"""Write a function that merges two sorted arrays into a single one. The arrays only contain integers. Also, the final outcome must be sorted and not have any duplicate."""

def merge_arrays(first, second):
    return sorted(set(first + second))


print(merge_arrays([1,2,5,7], [1, 3, 4, 2, 10]))
