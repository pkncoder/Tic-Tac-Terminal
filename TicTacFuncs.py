from random import randint

def printTable(slots):
    print(f"{slots[0]} | {slots[1]} | {slots[2]} \n{slots[3]} | {slots[4]} | {slots[5]}\n{slots[6]} | {slots[7]} | {slots[8]}")


def printTableNums():
    print(f"1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9")


def test(slots, win):
    if slots[0] == slots[1] == slots[2] != "-":
        win = True
        print(f"Congratulations {slots[0]} you WON!")

    elif slots[3] == slots[4] == slots[5] != "-":
        win = True
        print(f"Congratulation {slots[3]} you WON!")

    elif slots[6] == slots[7] == slots[8] != "-":
        win = True
        print(f"Congratulations {slots[6]} you WON!")

    elif slots[0] == slots[3] == slots[6] != "-":
        win = True
        print(f"Congratulations {slots[0]} you WON!")

    elif slots[1] == slots[4] == slots[7] != "-":
        win = True
        print(f"Congratulations {slots[1]} you WON!")

    elif slots[2] == slots[5] == slots[8] != "-":
        win = True
        print(f"Congratulations {slots[2]} you WON!")

    elif slots[0] == slots[4] == slots[8] != "-":
        win = True
        print(f"Congratulations {slots[0]} you WON!")

    elif slots[2] == slots[4] == slots[6] != "-":
        win = True
        print(f"Congratulations {slots[2]} you WON!")

    elif "-" not in slots:
        win = True
        print("It's a Tie")


    return win


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
