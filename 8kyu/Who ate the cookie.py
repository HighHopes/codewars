"""For this problem you must create a program that says who ate the last cookie. If the input is a string then "Zach" ate the cookie. If the input is a float or an int then "Monica" ate the cookie. If the input is anything else "the dog" ate the cookie. The way to return the statement is: "Who ate the last cookie? It was (name)!"

Ex: Input = "hi" --> Output = "Who ate the last cookie? It was Zach! (The reason you return Zach is because the input is a string)

Note: Make sure you return the correct message with correct spaces and punctuation."""


def cookie(x):
    return "Who ate the last cookie? It was {}!".format(
        "Zach" if type(x) == str else "the dog" if type(x) == bool else "Monica")


print(cookie("Ryan"))  # "Who ate the last cookie? It was Zach!")
print(cookie(2.3))  # "Who ate the last cookie? It was Monica!")
print(cookie(26))  # "Who ate the last cookie? It was Monica!")
print(cookie(True))  # "Who ate the last cookie? It was the dog!")
