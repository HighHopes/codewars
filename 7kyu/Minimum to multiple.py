"""Given two integers a and x, return the minimum non-negative number to add to / subtract from a to make it a multiple of x.

minimum(9, 8, Result) % Result = 1

% 9-1 = 8 which is a multiple of 4

minimum(10, 6, Result)  % Result = 2

% 10+2 = 12 which is a multiple of 6

Note

    0 is always a multiple of x
"""

def minimum(a, x):
    return min(a%x, x-a%x)

print(minimum(9, 4))  # 1
#print(minimum(150, 67))  # 16
