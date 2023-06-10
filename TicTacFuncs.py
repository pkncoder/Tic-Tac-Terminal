from random import randint

def printTable(slots):
    print("_______")
    print(f"|{slots[0]}|{slots[1]}|{slots[2]}|\n|{slots[3]}|{slots[4]}|{slots[5]}|\n|{slots[6]}|{slots[7]}|{slots[8]}|")
    print("-------")

def printTableNums():
    print("_______")
    print(f"|1|2|3|\n|4|5|6|\n|7|8|9|")
    print("-------")


def test(slots, win, usr1Cch, usr1sc, usr2sc):
    if slots[0] == slots[1] == slots[2] != "-":
        win = True
        print(f"Congratulations {slots[0]} you WON!")

        if slots[0] == usr1Cch:
            usr1sc += 1

        else:
            usr2sc += 1


    elif slots[3] == slots[4] == slots[5] != "-":
        win = True
        print(f"Congratulation {slots[3]} you WON!")

        if slots[3] == usr1Cch:
            usr1sc += 1

        else:
            usr2sc += 1


    elif slots[6] == slots[7] == slots[8] != "-":
        win = True
        print(f"Congratulations {slots[6]} you WON!")

        if slots[6] == usr1Cch:
            usr1sc += 1

        else:
            usr2sc += 1


    elif slots[0] == slots[3] == slots[6] != "-":
        win = True
        print(f"Congratulations {slots[0]} you WON!")

        if slots[0] == usr1Cch:
            usr1sc += 1

        else:
            usr2sc += 1


    elif slots[1] == slots[4] == slots[7] != "-":
        win = True
        print(f"Congratulations {slots[1]} you WON!")

        if slots[1] == usr1Cch:
            usr1sc += 1

        else:
            usr2sc += 1


    elif slots[2] == slots[5] == slots[8] != "-":
        win = True
        print(f"Congratulations {slots[2]} you WON!")

        if slots[2] == usr1Cch:
            usr1sc += 1

        else:
            usr2sc += 1


    elif slots[0] == slots[4] == slots[8] != "-":
        win = True
        print(f"Congratulations {slots[0]} you WON!")

        if slots[0] == usr1Cch:
            usr1sc += 1

        else:
            usr2sc += 1


    elif slots[2] == slots[4] == slots[6] != "-":
        win = True
        print(f"Congratulations {slots[2]} you WON!")
        
        if slots[2] == usr1Cch:
            usr1sc += 1

        else:
            usr2sc += 1


    elif "-" not in slots:
        win = True
        print("It's a Tie")


    return win, usr1sc, usr2sc


def startturn():
    int1 = randint(0, 21)
    rem1 = int1 % 2
    if rem1 == 0:
        return 'us1'
    
    else:
        return 'us2'
    
    
def turnflip(turn):
    if turn == 'us1':
        return 'us2'
    else:
        return 'us1'
