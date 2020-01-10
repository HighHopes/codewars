"""Given an array of integers , Find the minimum sum which is obtained from summing each Two integers product .

Notes
Array/list will contain positives only .
Array/list will always has even size
Input >> Output Examples
minSum({5,4,2,3}) ==> return (22)
Explanation:
The minimum sum obtained from summing each two integers product , 5*2 + 3*4 = 22"""

def min_sum(arr):
    lst = []
    while len(arr) > 0:
        arr_max = max(arr)
        arr_min = min(arr)
        prod = arr_max * arr_min
        lst.append(prod)
        arr.pop(arr.index(arr_max))
        arr.pop(arr.index(arr_min))
    lst_sum = sum(lst)
    return lst_sum

print(min_sum([5,4,2,3]))
