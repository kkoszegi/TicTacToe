import itertools

def newgame():
    x_player = input("Enter the name of Player1: ")
    o_player = input("Enter the name of Player2: ")
    players = [x_player, o_player]
    print(f"\nHello {players[0]} and {players[1]}!\nLet's play Tic Tac Toe!\n")

    return players

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

def choise(player, board):
    field = int(input(f"{player}! Choose a field on the board (1-9): "))
    while True:
        if board[field] == " ":
            return field
        else:
            field = int(input(f"{player}! Choose another field because it is occupied (1-9): "))

def victory(player, board):  # parameter 1: dictionary, parameter 2: "x"/"o", return: none/"x"/"o"
    if player == players[0]:
        xo = "x"
    elif player == players[1]:
        xo = "o"
    victs = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
    for vict in victs:
        if board[vict[0]] == board[vict[1]] == board[vict[2]] == xo:
            print(f"Nyert {player}!")
            return False

players = newgame()
player = players[0]
board = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
used_field_list = [] # This will hold all fields already used
x = None
print_board(board)
while x == None:
    field = choise(player, board)
    board = board_modify(player, board, field)
    print_board(board)
    x = victory(player, board)
    player = change_player(player, players)