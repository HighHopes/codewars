"""For every good kata idea there seem to be quite a few bad ones!

In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'. If there are one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'. If there are no good ideas, as is often the case, return 'Fail!'."""

def well(x):
    if x.count("good") == 0:
        return "Fail!"
    elif x.count("good") <= 2:
        return "Publish!"
    else:
        return 'I smell a series!'



print(well(['bad', 'bad', 'bad']))  # 'Fail!'
print(well(['good', 'bad', 'bad', 'bad', 'bad']))  # 'Publish!'
print(well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']))  # 'I smell a series!'
