"""Write a function that returns the total surface area and volume of a box as an array: [area, volume]."""


def get_size(w, h, d):
	sa = 2 * (h * w) + 2 * (h * d) + 2 * (w * d)
	v = w * h * d
	return [sa, v]
