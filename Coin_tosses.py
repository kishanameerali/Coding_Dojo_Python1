#Coin Tosses

"""
Write a function that simulates tossing a coin 5,000 times.
Your function should print how many times the head/tail appears.
"""

import random

def coin_toss(attempts):
    heads_total = 0
    tails_total = 0
    result = ""
    print "Starting the program..."
    for attempts in range(1, attempts + 1):
        flip = random.randint(1,11)
        if flip < 6:
            result = "It's a head!"
            heads_total = heads_total + 1
        else:
            result = "It's a tail!"
            tails_total = tails_total + 1
        print "Attempt #" + str(attempts) + ": Throwing the coin...",result,"... Got",heads_total,"head(s) so far and",tails_total,"tail(s) so far"
    print "Ending the program, thank you!"

coin_toss(5000)
