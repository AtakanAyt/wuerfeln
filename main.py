import random
import time


## würfel Blackjack
# Spielregeln: Du fängst an zu würfeln (Zahlen zwischen 1-6). Man darf so oft würfeln bis man entweder 18 erreicht oder
# die gessamt gewürfelte zahl 18 übersteigt.
# Will man nicht mehr würfeln oder ist über 18 (bust), würfelt der Computer so oft bis er bei zwischen 16-18 ankommt.
# Wer näher an der 18 ist gewinnt das spiel.

while True:
    start = input("Sollen wir anfangen? (y,n): ").lower()
    if start == "y":
        player = True
        computer = True
    else:
        print("bis zum nächsten mal!")
        break


    def würfeln():
        würfel_ergebnis = (random.randint(1, 6))
        print(f"Es wurde eine {würfel_ergebnis} gewürfelt!")
        return würfel_ergebnis


    def nochmal():
        again = input(f"du bist bei {player_counter} möchtest du nochmal würfeln? (y/n): ").lower()
        if again == "n":
            global player
            player = False

    def erneut_spielen():
        x = input("möchtest du nochmal spielen? (y/n): ")
        return x


    player_counter = 0
    while player:
        player_counter += würfeln()

        if player_counter > 18:
            print(f"Du bist bei {player_counter} und somit über 18, 'bust`!")
            break
        elif player_counter == 18:
            print("Super `PerfectDice`")
            break
        nochmal()

    computer_counter = 0


    # Computer würfelt bis er entweder über 18 ist oder zwischen 15 und 18 mit dem Score erreicht
    while computer:
        print("Der Computer würfelt jetzt:")
        if computer_counter <= 15:
            computer_counter += würfeln()
            print(f"Das Dicemonster ist gesammt bei {computer_counter}.")
            time.sleep(0)

        elif computer_counter == 18:
            print(f"Das Dicemonster hat einen `PerfectDice`!")
            break
        else:
            if computer_counter < 18:
                print(f"Das Dicemonster hat einen Score von {computer_counter}")
                break
            else:
                print(f"Das Dicemonster ist bei {computer_counter} und somit über 18, `bust`!")
                break

    print("--------Ergebnis-----------")

    # scores vergleichen
    print(f"Dein Score: {player_counter}, Dicemonster Score: {computer_counter}")
    if player_counter < 19 and computer_counter < 19:
        if player_counter < computer_counter:
            print("Dicemonster gewinnt diese Runde")
            x = erneut_spielen()
            if x == "n":
                break
        elif player_counter == computer_counter:
            print("Unentschieden!")
            x = erneut_spielen()
            if x == "n":
                break
        else:
            print("Glückwunsch, du gewinnst diese Runde")
            x =erneut_spielen()
            if x == "n":
                break
    elif player_counter > 18 and computer_counter > 18:
        print("Ihr seid beide über 18 Punkte gekommen, das Dicemonster gewinnt!")
        x = erneut_spielen()
        if x == "n":
            break
    elif player_counter < 19 and computer_counter > 18:
        print("'bust' vom Dicemonster, du gewinnst!")
        x =erneut_spielen()
        if x == "n":
            break
    else:
        print("yikes")










