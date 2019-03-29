"""Imagine you are creating a game where the user has to guess the correct number. But there is a limit of how many guesses the user can do.

If the user tries to guess WRONG more than the limit the function should throw an error
If the user guess wrong it should lose a life and return false (if you guess correctly you shouldn't remove a life)
If the user guess right it should return true"""


class Guesser(object):
	def __init__(self, number, lives):
		self.number = number
		self.lives = lives

	def guess(self, n):
		return False


guesser = Guesser(10, 2)
