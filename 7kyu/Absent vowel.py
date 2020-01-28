"""Your job is to figure out the index of which vowel is missing from a given string:

A has an index of 0,
E has an index of 1,
I has an index of 2,
O has an index of 3,
U has an index of 4.
Notes: There is no need for string validation and every sentence given will contain all vowles but one. Also, you won't need to worry about capitals.

Examples
"John Doe hs seven red pples under his bsket"          =>  0  ; missing: "a"
"Bb Smith sent us six neatly arranged range bicycles"  =>  3  ; missing: "o" """


def absent_vowel(x):
    vowels = ["a", "e", "i", "o", "u"]
    get_vowels = set(i for i in x if i in vowels)
    missing = "".join([i for i in vowels if i not in get_vowels])
    return vowels.index(missing)


print(absent_vowel("John Doe hs seven red pples under his bsket"))  # 0
print(absent_vowel("Bb Smith sent us six neatly arranged range bicycles"))  # 3
