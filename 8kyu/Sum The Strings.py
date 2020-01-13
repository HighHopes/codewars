"""Create a function that takes 2 positive integers in form of a string as an input, and outputs the sum (also as a string):

  sumStr("4", "5")    // should output "9"
  sumStr("34", "5")   // should output "39"
If either input is an empty string, consider it as zero."""


def sum_str(a, b):
    if a == '' and b == '': return '0'
    elif a == '': return b
    elif b == '': return a
    else: return str(int(a) + int(b))


print(sum_str("4","5"))  # "9"
print(sum_str("34","5"))  # "39"
