def loves(name1, name2):
    names = (name1 + name2).replace(" ", "").lower()
    print(names)
    
    result = ""
    temp = ""
    
    for i in "loves":
        result += str(names.count(i))
    
    return result


print(loves("John Doe", "Jane Doe"))  # 66%
