"""Two players - "black" and "white" are playing a game. The game consists of several rounds. If a player wins in a round, he is to move again during the next round. If a player loses a round, it's the other player who moves on the next round. Given whose turn it was on the previous round and whether he won, determine whose turn it is on the next round.

Example
For lastPlayer = "black" and win = false, the output should be "white".

For lastPlayer = "white" and win = true, the output should be "white"."""


def whoseMove(lastPlayer, win):
    return "white" if lastPlayer == "black" and win == False or lastPlayer == "white" and win == True else "black"


print(whoseMove('black', False))  # 'white'
print(whoseMove('white', False))  # 'black'
print(whoseMove('black', True))  # 'black'
print(whoseMove('white', True))  # 'white'
