"""You work in the best consumer electronics corporation, and your boss wants to find out which three products generate the most revenue. Given 3 lists of the same length like these:

products: ["Computer", "Cell Phones", "Vacuum Cleaner"]
amounts: [3, 24, 8]
prices: [199, 299, 399]
return the three product names with the highest revenue (amount * price).

Note: if multiple products have the same revenue, order them according to their original positions in the input list."""


def top3(products, amounts, prices):
    lst = sorted(list(zip(products, [i*j for i, j in list(zip(amounts, prices))])), key=lambda tup: tup[1], reverse=True)[0:3]

    return [lst[i][0] for i in range(3)]


print(top3(["Computer", "Cell Phones", "Vacuum Cleaner"], [3,24,8], [199,299,399])) # ["Cell Phones", "Vacuum Cleaner", "Computer"]
print(top3(["Cell Phones", "Vacuum Cleaner", "Computer", "Autos", "Gold", "Fishing Rods", "Lego", " Speakers"], [5, 25, 2, 7, 10, 3, 2, 24], [51, 225, 22, 47, 510, 83, 82, 124])) # ['Vacuum Cleaner', 'Gold', ' Speakers']
print(top3(["Cell Phones", "Vacuum Cleaner", "Computer", "Autos", "Gold", "Fishing Rods", "Lego", " Speakers"], [0, 12, 24, 17, 19, 23, 120, 8], [9, 24, 29, 31, 51, 8, 120, 14])) # ['Lego', 'Gold', 'Computer']
