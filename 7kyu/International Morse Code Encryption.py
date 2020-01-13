"""Write a function that will encrypt a given sentence into International Morse Code, both the input and out puts will be strings.

Characters should be separated by a single space. Words should be separated by a triple space.

For example, "HELLO WORLD" should return -> ".... . .-.. .-.. --- .-- --- .-. .-.. -.."

A preloaded object/dictionary/hash called CHAR_TO_MORSE will be provided to help convert characters to Morse Code."""


CHAR_TO_MORSE = {'0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', 'a': '.-', 'h': '....', 'o': '---', 'u': '..-', 'b': '-...', 'i': '..', 'p': '.--.', 'v': '...-', 'c': '-.-.', 'j': '.---', 'q': '--.-', 'w': '.--', 'd': '-..', 'k': '-.-', 'r': '.-.', 'x': '-..-', 'e': '.', 'l': '.-..', 's': '...', 'y': '-.--', 'f': '..-.', 'm': '--', 't': '-', 'z': '--..', 'g': '--.', 'n': '-.', 'A': '.-', 'H': '....', 'O': '---', 'U': '..-', 'B': '-...', 'I': '..', 'P': '.--.', 'V': '...-', 'C': '-.-.', 'J': '.---', 'Q': '--.-', 'W': '.--', 'D': '-..', 'K': '-.-', 'R': '.-.', 'X': '-..-', 'E': '.', 'L': '.-..', 'S': '...', 'Y': '-.--', 'F': '..-.', 'M': '--', 'T': '-', 'Z': '--..', 'G': '--.', 'N': '-.'}


def encryption(string):
    result = ""
    for i in string:
        if i != " ":
            result += CHAR_TO_MORSE[i] + " "
        else:
            result += "  "

    return result.strip()


print(encryption("oUVu30h6LANZ  GG"))
