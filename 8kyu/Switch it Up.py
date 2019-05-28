"""When provided with a number between 0-9, return it in words.

Input :: 1
Output :: "One".

Try using "Switch" statements."""


def switch_it_up(number):
  dict = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
  return dict[number]


print(switch_it_up(9))
