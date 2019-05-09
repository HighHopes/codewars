"""Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']"""


def anagrams(word, words):
	return [i for i in words if len(i) == len(word) and ''.join(sorted(i)) == ''.join(sorted(word))]
