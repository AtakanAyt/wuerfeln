import random

start = input("Hola, möchtest du würfeln? (y,n): ").lower()
if start == "y":
    play = True
else:
    play = False


def würfeln():
    print(random.randint(1, 7))


def nochmal():
    again = input("möchtest du nochmal würfeln? (y/n): ").lower()
    if again == "n":
        global play
        play = False
        return play



while play:
    würfeln()
    nochmal()

