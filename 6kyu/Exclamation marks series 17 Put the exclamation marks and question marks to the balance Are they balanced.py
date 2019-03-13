"""Each exclamation mark weight is 2; Each question mark weight is 3. Put two string left and right to the balance, Are they balanced?

If the left side is more heavy, return "Left"; If the right side is more heavy, return "Right"; If they are balanced, return "Balance".

Examples
balance("!!","??") == "Right"
balance("!??","?!!") == "Left"
balance("!?!!","?!?") == "Left"
balance("!!???!????","??!!?!!!!!!!") == "Balance"
Note
Please don't post issue about difficulty or duplicate."""


def balance(left, right):
	left_weight = left.count("!") * 2 + left.count("?") * 3
	right_weight = right.count("!") * 2 + right.count("?") * 3
	if left_weight > right_weight:
		return "Left"
	elif right_weight > left_weight:
		return "Right"
	else:
		return "Balance"
