from TicTacFuncs import printTable, printTableNums, test, startturn, turnflip

slots = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
errors = 0

win = False
ster1 = True
ster2 = True

turn = startturn()

usr1n = input("What is your name, player one: ")

while ster1 == True:

    usr1Cch = input(f"What is your letter, or character choice {usr1n} (only one character/letter please): ")

    if len(usr1Cch) > 1:
        print("That is more than one character or letter, please choose again.")
        errors += 1
        

    else:
        print("Player one has been created for this game!")
        ster1 = False


usr2n = input("what is your name, player two: ")

while ster2 == True:
    usr2Cch = input(f"What is your letter, or character choice {usr2n} (only one character/letter please): ")

    if len(usr2Cch) > 1:
        print("That is more than one character or letter, please choose again.")
        errors += 1
    

    elif usr1Cch == usr2Cch:
        print("That is the same character as Player one, please choose somthing else (you can play with uppercase and lowercase).")
        errors += 1


    else:
        print("Player two has been created for this game, let's go!")
        ster2 = False


while win == False:
    if turn == 'us1':
        printTable(slots)
        printTableNums()
        us1ch = int(input(f"What is your choice {usr1n}? Use numbers 1 to 9 to take your pick. Numbers are shown on the second table: "))

        if us1ch >= 10:
            print("Sorry, that's out of the range of the table, please try again.")
            i = 1
            errors += 1

        else:
            if slots[us1ch - 1] == '-':
                slots[us1ch - 1] = usr1Cch
                i = 0

            else:
                print("Sorry, that tile is already taken. Please try again.")
                i = 1
                errors += 1


        if i != 1:
            turn = turnflip(turn)


        win = test(slots, win)

    elif turn == 'us2':
        i = 0
        printTable(slots)
        printTableNums()
        us2ch = int(input(f"What is your choice {usr2n}? Use numbers 1 to 9 to take your pick. Numbers are shown on the second table: "))

        if us2ch >= 10:
            print("Sorry, that's out of the range of the table, please try again.")
            i = 1
            errors += 1
        
        else:
            if slots[us2ch - 1] == '-':
                slots[us2ch - 1] = usr2Cch
                i = 0
                
            else:
                print("Sorry, that tile is already taken. Please try again.")
                i = 1
                errors += 1


        if i != 1:
            turn = turnflip(turn)


        win = test(slots, win)


printTable(slots)

if errors == 0:
    endpunc = '!'
    endsornos = "s"

elif errors == 1:
    endpunc = "."
    endsornos = ""

else:
    endpunc = "."
    endsornos = "s"


print(f"Good game! There were {errors} invalid response{endsornos}{endpunc}")
