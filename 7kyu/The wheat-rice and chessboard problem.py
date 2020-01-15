"""I assume most of you are familiar with the ancient legend of the rice (but I see wikipedia suggests wheat, for some reason) problem, but a quick recap for you: a young man asks as a compensation only 1 grain of rice for the first square, 2 grains for the second, 4 for the third, 8 for the fourth and so on, always doubling the previous.

Your task is pretty straightforward (but not necessarily easy): given an amount of grains, you need to return up to which square of the chessboard one should count in order to get at least as many.

As usual, a few examples might be way better than thousands of words from me:

squares_needed(0) == 0
squares_needed(1) == 1
squares_needed(2) == 2
squares_needed(3) == 2
squares_needed(4) == 3"""


def squares_needed(grains):
    if grains == 0: return 0
    p = 1
    while pow(2, p) <= grains:
        p += 1
    return p

print(squares_needed(0))  #0
print(squares_needed(1))  #1
#print(squares_needed(2))  #2
print(squares_needed(3))  #2
#print(squares_needed(4))  #3
print(squares_needed(5))  #3
print(squares_needed(7))  #3
print(squares_needed(16))  #5
