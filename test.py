def row_sum_odd_numbers(n):
    a = []
    x = 1
    y = 1
    while len(a) < n:
        temp = []
        for i in range(x, y):
            temp.append(i)
        a.append(temp)

    return a


#print(row_sum_odd_numbers(1))  # 1
#print(row_sum_odd_numbers(2))  # 8
print(row_sum_odd_numbers(5))  # 2197
#print(row_sum_odd_numbers(19))  # 6859
#print(row_sum_odd_numbers(41))  # 68921
