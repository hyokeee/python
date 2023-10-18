from random import random
def printHelloBye():
    rnd = random()
    if rnd > 0.5:
        print("Hello")
    else:
        print("Bye")

printHelloBye()