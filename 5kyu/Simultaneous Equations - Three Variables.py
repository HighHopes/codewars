"""
We have 3 equations with 3 unknowns x, y, and z and we are to solve for these unknowns.

Equations 4x -3y +z = -10, 2x +y +3z = 0, and -x +2y -5z = 17 will be passed in as an array of [[4, -3, 1, -10], [2, 1, 3, 0], [-1, 2, -5, 17]] and the result should be returned as an array like [1, 4, -2] (i.e. [x, y, z]).
"""


def solve_eq(eq):
	# Cramer's Rule

	# eq det
	d = eq[0][0] * eq[1][1] * eq[2][2] + eq[1][0] * eq[2][1] * eq[0][2] + eq[0][1] * eq[1][2] * eq[2][0] - (
			eq[2][0] * eq[1][1] * eq[0][2] + eq[2][1] * eq[1][2] * eq[0][0] + eq[1][0] * eq[0][1] * eq[2][2])

	dx = eq[0][3] * eq[1][1] * eq[2][2] + eq[1][3] * eq[2][1] * eq[0][2] + eq[0][1] * eq[1][2] * eq[2][3] - (
			eq[2][3] * eq[1][1] * eq[0][2] + eq[2][1] * eq[1][2] * eq[0][3] + eq[1][3] * eq[0][1] * eq[2][2])
	dy = eq[0][0] * eq[1][3] * eq[2][2] + eq[1][0] * eq[2][3] * eq[0][2] + eq[0][3] * eq[1][2] * eq[2][0] - (
			eq[2][0] * eq[1][3] * eq[0][2] + eq[2][3] * eq[1][2] * eq[0][0] + eq[1][0] * eq[0][3] * eq[2][2])
	dz = eq[0][0] * eq[1][1] * eq[2][3] + eq[1][0] * eq[2][1] * eq[0][3] + eq[0][1] * eq[1][3] * eq[2][0] - (
			eq[2][0] * eq[1][1] * eq[0][3] + eq[2][1] * eq[1][3] * eq[0][0] + eq[1][0] * eq[0][1] * eq[2][3])

	x = dx / d
	y = dy / d
	z = dz / d

	return [int(x), int(y), int(z)]
