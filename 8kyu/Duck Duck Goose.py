"""The objective of 'Duck, duck, goose' is to walk in a circle, tapping on each player's head until one is finally chosen.

Task: Given an array of Player objects (an array of associative arrays in PHP) and an index (1-based), return the name of the chosen Player.

Example:

`duck_duck_goose([a, b, c, d], 1) should return a.name` `duck_duck_goose([a, b, c, d], 5) should return a.name` `duck_duck_goose([a, b, c, d], 4) should return d.name`
// PHP only
duck_duck_goose([$a, $b, $c, $d], 1); // => $a["name"]
duck_duck_goose([$a, $b, $c, $d], 5); // => $a["name"]
duck_duck_goose([$a, $b, $c, $d], 4); // => $d["name"]"""


def duck_duck_goose(players, goose):
	count = 0
	pos = 0
	while count < len(players):
		if pos == goose:
			return players[count - 1].name
		count += 1

		if count >= len(players):
			count = 0

		pos += 1
