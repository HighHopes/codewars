"""Your task is to find the nearest square number, nearest_sq(n), of a positive integer n."""


from math import sqrt

def nearest_sq(n):
    return pow(round(sqrt(n)), 2)
