"""If the wolf is the closest animal to you, return "Pls go away and stop eating my sheep". Otherwise, return "Oi! Sheep number N! You are about to be eaten by a wolf!" where N is the sheep's position in the queue.

Note: there will always be exactly one wolf in the array.

Examples
warn_the_sheep(["sheep", "sheep", "sheep", "wolf", "sheep"]) == 'Oi! Sheep number 1! You are about to be eaten by a wolf!'

warn_the_sheep(['sheep', 'sheep', 'wolf']) == 'Pls go away and stop eating my sheep'"""


def warn_the_sheep(queue):
    if queue[-1] == "wolf": return "Pls go away and stop eating my sheep"
    return 'Oi! Sheep number {}! You are about to be eaten by a wolf!'.format(list(reversed(queue)).index("wolf"))
