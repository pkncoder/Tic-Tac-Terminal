from TicTacFuncs import printTable, printTableNums, test, startturn, turnflip

slots = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
win = False
errors = 0

turn = startturn()

usr1n = input("What is your name, player one: ")
usr1Cch = input(f"What is your letter, or character choice {usr1n} (only one character/letter please): ")
usr2n = input("what is your name, player two: ")
usr2Cch = input(f"What is your letter, or character choice {usr2n} (only one character/letter please): ")

while win == False:
    if turn == 'us1':
        printTable(slots)
        printTableNums()
        us1ch = int(input(f"What is your choice {usr1n}? 1 to 9, shown as the second table: "))

        if us1ch >= 10:
            print("Sorry, that's out of the range of the table, please try again")
            i = 1
            errors += 1

        else:
            if slots[us1ch - 1] == '-':
                slots[us1ch - 1] = usr1Cch
                i = 0

            else:
                print("Nope, that's not allowed. Wrong input please try again.")
                i = 1
                errors += 1


        if i != 1:
            turn = turnflip(turn)


        win = test(slots, win)

    elif turn == 'us2':
        i = 0
        printTable(slots)
        printTableNums()
        us2ch = int(input(f"What is your choice {usr2n}? 1 to 9, shown as the second table: "))

        if us2ch >= 10:
            print("Sorry, that's out of the range of the table, please try again")
            i = 1
            errors += 1
        
        else:
            if slots[us2ch - 1] == '-':
                slots[us2ch - 1] = usr2Cch
                i = 0
                
            else:
                print("Nope, that's not allowed. Wrong input please try again")
                i = 1
                errors += 1


        if i != 1:
            turn = turnflip(turn)


        win = test(slots, win)


printTable(slots)
print(f"Good game! There were {errors} number of invalid responses.")
