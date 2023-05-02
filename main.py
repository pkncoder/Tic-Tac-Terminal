from TicTacFuncs import *

board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

GameOn = True

player = 'P1'

printboard(board)

while GameOn != False:
    if player == 'P1':
        P1Choice = int(input('Pick from 1-9, Player 1: '))
        board[P1Choice - 1] = 'X'
        player = playerflip(player)
    elif player == 'P2':
        P2Choice = int(input('Pick from 1-9, Player 2: '))
        board[P2Choice - 1] = 'O'
        player = playerflip(player)
    printboard(board)
    GameOn = testwin(board, GameOn)