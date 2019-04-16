def infect_apple(apple, n):
	if n == 0:
		return apple
	else:
		for i in range(0, len(apple)):
			for j in range(0, len(apple[i])):
				if i == 0 and j == 0 and apple[i][j] == "V":
					apple[i][j + 1] = "V"
					apple[i + 1][j] = "V"
				elif i > 0 and i < len(apple) - 1 and j == 0 and apple[i][j] == "V":
					apple[i - 1][j] = "V"
					apple[i][j + 1] = "V"
					apple[i + 1][j] = "V"
	return apple


# apple = [["A", "A", "A", "A", "A"], ["V", "A", "A", "A", "A"], ["A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A"]]
# print(infect_apple(apple, 0))


apple = [["V", "A", "A", "A", "A"], ["V", "A", "A", "A", "A"], ["A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A"],
		 ["A", "A", "A", "A", "A"]]
print(infect_apple(apple, 2))
