"""Given an array/list [] of integers , Find the product of the k maximal numbers.

Notes
Array/list size is at least 3 .

Array/list's numbers Will be mixture of positives , negatives and zeros

Repetition of numbers in the array/list could occur.

Input >> Output Examples
maxProduct ({4, 3, 5}, 2) ==>  return (20)
Explanation:
Since the size (k) equal 2 , then the subsequence of size 2 whose gives product of maxima is 5 * 4 = 20 ."""

def max_product(lst, n_largest_elements):
    sort = sorted(lst, reverse=True)[0:n_largest_elements]
    prod = 1
    for i in sort:
        prod = prod * i
    return prod


print(max_product([0]*10, 5))  # 0
print(max_product([4,3,5], 2))  # 20
print(max_product([10,8,7,9], 3))  # 720
