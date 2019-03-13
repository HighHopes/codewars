"""
Once upon a time, on a way through the old wild west,… a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too. Going to one direction and coming back the opposite direction is a needless effort. Since this is the wild west, with dreadfull weather and not much water, it's important to save yourself some energy, otherwise you might die of thirst!

How I crossed the desert the smart way.
The directions given to the man are, for example, the following:

["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].

You can immediatly see that going "NORTH" and then "SOUTH" is not reasonable, better stay to the same place! So the task is to give to the man a simplified version of the plan. A better plan in this case is simply:

["WEST"]
"""


def dirReduc(arr):
	counter = 0

	while counter < len(arr) - 1:
		if (arr[counter] == "NORTH" and arr[counter + 1] == "SOUTH") or (
				arr[counter] == "SOUTH" and arr[counter + 1] == "NORTH") or (
				arr[counter] == "EAST" and arr[counter + 1] == "WEST") or (
				arr[counter] == "WEST" and arr[counter + 1] == "EAST"):
			del arr[counter + 1]
			del arr[counter]
			counter = 0
		else:
			counter += 1

	return arr
