"""Suppose we know the process (A) by which a string s has been coded to a string r.

The aim of the kata is to decode r to get back the original string s.

Explanation of the known process (A):
data: a string s composed of lowercase letters from a to z and a positive integer num

we know there is a correspondence between abcde...uvwxyzand 0, 1, 2 ..., 23, 24, 25 : 0 <-> a, 1 <-> b ...

if c is a character of s whose corresponding number is x, apply to x the function f: x-> f(x) = num * x % 26 then find ch the corresponding character of f(x)

Accumulate all these ch in a string r.

concatenate num and r and return the result.

Example:
code("mer", 6015) -> "6015ekx"
m <-> 12, 12 * 6015 % 26 == 4, 4 <-> e
e <-> 4, 4 * 6015 % 26 == 10, 10 <-> k
r <-> 17, 17 * 6015 % 26 == 23, 23 <-> x
We get "ekx" hence "6015ekx"
Task
A string s has been coded to a string r by the above process (A). Write a function r -> decode(r) to get back s whenever it is possible.

Indeed it can happen that the decoding is impossible when positive integer num has not been correctly chosen. In that case return "Impossible to decode".

Example:
decode("6015ekx") -> "mer"
decode("5057aan") -> "Impossible to decode" """


def decode(r):
    num = int("".join([i for i in r if i.isdigit()]))
    strng = [i for i in r if i.isalpha()]
    init = []
    
    for j in [ord(i) - 97 for i in strng]:
        for i in [i for i in range(0, 26)]:
            if i * num % 26 == j:
                init.append(i)
    
    result = ""
    
    for i in init:
        result += chr(i + 97)
    
    if len(strng) == len(result):
        return result
    else:
        return "Impossible to decode"


print(decode("6015ekx"))  # mer
print(decode("1273409kuqhkoynvvknsdwljantzkpnmfgf"))  # uogbucwnddunktsjfanzlurnyxmx
print(decode("5057aan"))  # Impossible to decode
print(decode("761328qockcouoqmoayqwmkkic"))  # Impossible to decode
