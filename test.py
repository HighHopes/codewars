def add_letters(*letters):
    if len(letters) == 0:
        return "z"
    else:
        s = 0
        for i in letters:
            for j in i:
                s += ord(j)-96
        return chr(s+96), s

print(add_letters(["a", "b", "c"]))
print(add_letters(["a", "b"]))
print(add_letters(['z', 'a']))
print(add_letters([]))
