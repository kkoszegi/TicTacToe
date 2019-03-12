import itertools

def newgame():
    x_player = input("Enter the name of Player1: ")
    o_player = input("Enter the name of Player2: ")
    players = [x_player, o_player]
    print(f"\nHello {players[0]} and {players[1]}!\nLet's play Tic Tac Toe!\n")

    return players

used_field = [] # This will hold all fields already used

#used_field.append()

def change_player(player, players):
    if player == players[1]:
        return players[0]
    elif player == players[0]:
        return players[1]

def board_modify(player, board, field):
    if player == players[0]:
        board[field] = "x"
    elif player == players[1]:
        board[field] = "o"
    return board

# the board
def print_board(board):
    print(' _____ _____ _____')
    print('|     |     |     |')
    print('|  ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3] + '  |')
    print('|_____|_____|_____|')
    print('|     |     |     |')
    print('|  ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6] + '  |')
    print('|_____|_____|_____|')
    print('|     |     |     |')
    print('|  ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9] + '  |')
    print('|_____|_____|_____|')
    print('\n')

def choise(player):
    field = int(input(f"{player}! Choose a field on the board (1-9)."))
    return field

players = newgame()
player = players[0]
board = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
while True:
    print_board(board)
    field = choise(player)
    board = board_modify(player, board, field)
    player = change_player(player, players)