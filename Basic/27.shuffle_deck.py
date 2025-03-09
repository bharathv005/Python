#Shuffle the deck of cards

import random,itertools

deck = list(itertools.product(range(1,14),["Spade","Club","Heart","Diamond"]))

random.shuffle(deck)

for i in range(5):
    print(deck[i][0],end=" of ")
    print(deck[i][1])
    