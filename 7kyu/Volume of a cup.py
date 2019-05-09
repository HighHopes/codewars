"""Your job is to return the volume of a cup when given the diameter of the top, the diameter of the bottom and the height.

You know that there is a steady gradient from the top to the bottom.

You want to return the volume rounded to 2 decimal places."""

import math


def cup_volume(d1, d2, height):
	return round(
		(math.pi * float(height)) * ((float(d1) / 2) ** 2 + (float(d2) / 2) ** 2 + (float(d1) / 2 * float(d2) / 2)) / 3,
		2)


print(cup_volume(1, 1, 1))  # 0.79
print(cup_volume(10, 8, 10))  # 638.79
print(cup_volume(5, 12, 31))  # 1858.51
