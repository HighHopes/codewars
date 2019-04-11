"""Take a number: 56789. Rotate left, you get 67895.

Keep the first digit in place and rotate left the other digits: 68957.

Keep the first two digits in place and rotate the other ones: 68579.

Keep the first three digits and rotate left the rest: 68597. Now it is over since keeping the first four it remains only one digit which rotated is itself.

You have the following sequence of numbers:

56789 -> 67895 -> 68957 -> 68579 -> 68597

and you must return the greatest: 68957.

Task
Write function max_rot(n) which given a positive integer n returns the maximum number you got doing rotations similar to the above example."""


def max_rot(n):
	lst = [i for i in str(n)]
	rot = 0
	new_lst = []
	while rot < len(lst):
		new_lst.append(int("".join(lst)))
		lst.append(lst.pop(rot))
		rot += 1
	return max(new_lst)


print(max_rot(56789))  # 68957
print(max_rot(38458215))  # 85821534
