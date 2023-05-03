from TicTacFuncs import playerflip, printboard, testwin

board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

GameOn = True

player = 'P1'

print("Welcome to Tic-Tac-Terminal. This is Tic-Tac-Toe but, as the name states, in the terminal.")

P1Char = input("Player 1, what character do you want to use (Letters or Symbals please): ")
P2Char = input("Player 2, what character do you want to use (Letters or Symbals please): ")

printboard(board)

while GameOn != False:
    if player == 'P1':

        P1Choice = int(input('Pick from 1-9, Player 1: '))

        if board[P1Choice - 1] != '-':
            print("This square is already taken!")

        else:
            board[P1Choice - 1] = P1Char
            player = playerflip(player)

    elif player == 'P2':

        P2Choice = int(input('Pick from 1-9, Player 2: '))

        if board[P2Choice - 1] != '-':
            print("This square is already taken")

        else:
            board[P2Choice - 1] = P2Char
            player = playerflip(player)

    printboard(board)

    GameOn = testwin(board, GameOn)