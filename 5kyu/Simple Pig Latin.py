"""Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !"""


def pig_it(text):
    result = ""
    
    for i in [i for i in text.split()]:
        if i.isalpha():
            result += i[1:] + i[0] + "ay" + " "
        else:
            result += i + " "
    
    return result.strip()


print(pig_it('Pig latin is cool'))  # 'igPay atinlay siay oolcay'
print(pig_it('0 tempora o mores !'))  # '0 emporatay oay oresmay !'
