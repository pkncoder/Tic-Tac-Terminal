def printboard(board):
    print(f'{board[0]} | {board[1]} | {board[2]}    1|2|3')
    print(f'{board[3]} | {board[4]} | {board[5]}    4|5|6')
    print(f'{board[6]} | {board[7]} | {board[8]}    7|8|9')

def testwin(board, GameOn):
    if board[0] == board[1] == board[2] != "-":
        GameOn = False
        print(f"Congratulations {board[0]} you WON!")
    elif board[3] == board[4] == board[5] != "-":
        GameOn = False
        print(f"Congratulations {board[3]} you WON!")
    elif board[6] == board[7] == board[8] != "-":
        GameOn = False
        print(f"Congratulations {board[6]} you WON!")
    elif board[0] == board[3] == board[6] != "-":
        GameOn = False
        print(f"Congratulations {board[0]} you WON!")
    elif board[1] == board[4] == board[7] != "-":
        GameOn = False
        print(f"Congratulations {board[1]} you WON!")
    elif board[2] == board[5] == board[8] != "-":
        GameOn = False
        print(f"Congratulations {board[2]} you WON!")
    elif board[0] == board[4] == board[8] != "-":
        GameOn = False
        print(f"Congratulations {board[0]} you WON!")
    elif board[2] == board[4] == board[6] != "-":
        GameOn = False
        print(f"Congratulations {board[2]} you WON!")
    elif "-" not in board:
        GameOn = False
        print("It's a Tie")
    return GameOn

def playerflip(player):
    if player == 'P1':
        player = 'P2'
    elif player == 'P2':
        player = 'P1'
    return player