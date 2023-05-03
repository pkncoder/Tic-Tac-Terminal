from TicTacFuncs import playerflip, printboard, testwin

board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

GameOn = True

player = 'P1'

printboard(board)

while GameOn != False:
    if player == 'P1':
        P1Choice = int(input('Pick from 1-9, Player 1: '))
        if board[P1Choice - 1] != '-':
            print("This square is already taken!")
        else:
            board[P1Choice - 1] = 'X'
            player = playerflip(player)
    elif player == 'P2':
        P2Choice = int(input('Pick from 1-9, Player 2: '))
        if board[P2Choice - 1] != '-':
            print("This square is already taken")
        else:
            board[P2Choice - 1] = 'O'
            player = playerflip(player)
    printboard(board)
    GameOn = testwin(board, GameOn)