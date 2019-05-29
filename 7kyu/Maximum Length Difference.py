def mxdiflg(a1, a2):
    if a1 == [] or a2 == []:
        return -1
    else:
        get_min = len(a1[0])
        for i in a1:
            if len(i) < get_min:
                get_min = len(i)
        
        get_max = len(a2[0])
        for i in a2:
            if len(i) > get_max:
                get_max = len(i)
        
        return abs(get_min - get_max)


s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
print(mxdiflg(s1, s2))  # 13
