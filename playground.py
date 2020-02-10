from itertools import permutations, product

def get_pins(observed):
    dct = {1: [1, 2, 4],
           2: [1, 2, 3, 5],
           3: [2, 3, 6],
           4: [1, 4, 5, 7],
           5: [2, 4, 5, 6, 7],
           6: [3, 5, 6, 9],
           7: [4, 7, 8],
           8: [0, 5, 7, 8, 9],
           9: [6, 8, 9],
           0: [0, 8]}

    if len(observed) == 1:
        return list(map(str, dct.get(int(observed))))

    lst = []

    for i in observed:
        lst.append(dct.get(int(i)))

    result = []

    for i in range(len(lst[0])):
        temp = ""
        temp += str(lst[0][i])

    print(temp)

    return None


print(get_pins("369"))


# 11
a = ["11", "22", "44", "12", "21", "14", "41", "24", "42"]

#369
b = ['236', '238', '239', '256', '258', '259', '266', '268', '269', '296', '298', '299', '336', '338', '339', '356', '358', '359', '366', '368', '369', '396', '398', '399', '636', '638', '639', '656', '658', '659', '666', '668', '669', '696', '698', '699']

# 58
c = ['20', '25', '27', '28', '29', '40', '45', '47', '48', '49', '50', '55', '57', '58', '59', '60', '65', '67', '68', '69', '80', '85', '87', '88', '89']

# print(len(b))