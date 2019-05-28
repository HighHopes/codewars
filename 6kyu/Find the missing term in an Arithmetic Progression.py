"""An Arithmetic Progression is defined as one in which there is a constant difference between the consecutive terms of a given series of numbers. You are provided with consecutive elements of an Arithmetic Progression. There is however one hitch: exactly one term from the original series is missing from the set of numbers which have been given to you. The rest of the given series is the same as the original AP. Find the missing term.

You have to write the function findMissing(list), list will always be at least 3 numbers. The missing term will never be the first or last one.

Example
find_missing([1, 3, 5, 9, 11]) == 7"""


def find_missing(sequence):
  if sequence[1] - sequence[0] == sequence[2] - sequence[1]:
    prog = sequence[1] - sequence[0]
  else:
    prog = sequence[3] - sequence[2]
  
  fin = list(range(sequence[0], sequence[-1] + prog, prog))
  result = [i for i in fin if i not in sequence]
  return result


print(find_missing([1, 2, 3, 4, 6, 7, 8, 9]))  # 5
print(find_missing([1, 3, 4, 5, 6, 7, 8, 9]))  # 2
