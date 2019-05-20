def define_suit(card):
    dict = {"c": "clubs", "d": "diamonds", "h": "hearts", "s": "spades"}
    return dict[card[-1].lower()]


print(define_suit('QS'))  # spades
