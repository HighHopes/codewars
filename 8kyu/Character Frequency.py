"""Your function will be called char_freq/charFreq/CharFreq and you will get passed a string, you will then return a dictionary (object in JavaScript) with as keys the characters, and as values how many times that character is in the string. You can assume you will be given valid input."""

def char_freq(message):
    dict = {}
    for i in message:
        if i in dict.keys():
            dict[i] += 1
        else:
            dict[i] = 1
    return dict


print(char_freq("I like cats"))
