"""In this kata you will have to write a function that takes litres and pricePerLiter as arguments. Purchases of 2 or more litres get a discount of 5 cents per litre, purchases of 4 or more litres get a discount of 10 cents per litre, and so on every two litres, up to a maximum discount of 25 cents per litre. But total discount per liter cannot be more than 25 cents. round answer to 2 decimal places. Also you can guess that there will not be negative or non-numeric inputs.

Good Luck!"""


def fuel_price(litres, price_per_liter):
	if litres >= 2 and litres < 4:
		discount = litres * 0.05
		return (litres * price_per_liter) - discount
	elif litres >= 4 and litres < 6:
		discount = litres * 0.10
		return (litres * price_per_liter) - discount
	elif litres >= 6 and litres < 8:
		discount = litres * 0.15
		return (litres * price_per_liter) - discount
	elif litres >= 8 and litres < 10:
		discount = litres * 0.20
		return (litres * price_per_liter) - discount
	else:
		discount = litres * 0.25
		return (litres * price_per_liter) - discount
