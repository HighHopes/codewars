<<<<<<< HEAD
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
=======
print("say:", input(":"))
>>>>>>> 7dd7ddd0a70fbeeeec2a29f6aad60c7bb48750a7
