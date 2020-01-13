"""Write these two functions
and

high-order function oper(fct, s) where

fct is the function of one variable f to apply to the string s (fct will be one of vertMirror, horMirror)
#Examples:

s = "abcd\nefgh\nijkl\nmnop"
oper(vert_mirror, s) => "dcba\nhgfe\nlkji\nponm"
oper(hor_mirror, s) => "mnop\nijkl\nefgh\nabcd" """


def vert_mirror(strng):
    return "\n".join([i[::-1] for i in strng.split("\n")])

def hor_mirror(strng):
    return "\n".join([i for i in strng.split("\n")][::-1])

def oper(fct, s):
    return fct(s)


#print(vert_mirror("hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu"))
#print(hor_mirror("hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu"))
print(oper(vert_mirror(), s))
