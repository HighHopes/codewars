"""Everyone knows passphrases. One can choose passphrases from poems, songs, movies names and so on but frequently they can be guessed due to common cultural references. You can get your passphrases stronger by different means. One is the following:

choose a text in capital letters including or not digits and non alphabetic characters,

1. shift each letter by a given number but the transformed letter must be a letter (circular shift),
2. replace each digit by its complement to 9,
3. keep such as non alphabetic and non digit characters,
4. downcase each letter in odd position, upcase each letter in even position (the first character is in position 0),
5. reverse the whole result.
#Example:

your text: "BORN IN 2015!", shift 1

1 + 2 + 3 -> "CPSO JO 7984!"

4 "CpSo jO 7984!"

5 "!4897 Oj oSpC"

With longer passphrases it's better to have a small and easy program. Would you write it?"""


def play_pass(s, n):
	lst = []

	for i in s:
		if i.isalpha():
			x = ord(i) + n
			if x > 90:
				x = x - 90 + 64
				lst.append(chr(x))
			else:
				lst.append(chr(ord(i) + n))
		if i.isdigit():
			lst.append(str(9 - int(i)))
		if not i.isalpha() and not i.isdigit():
			lst.append(i)

	for index, item in enumerate(lst):
		if index % 2 != 0:
			lst[index] = item.lower()
	lst = reversed(lst)

	return "".join(lst)


print(play_pass("I [**  LOVE YOU 1239!!!", 1))  # "!!!vPz fWpM J"
print(play_pass("BORN IN 2015!", 1))  # "BORN IN 2015!
