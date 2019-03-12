def newgame():
    x_player = input("Enter the name of Player1: ")
    o_player = input("Enter the name of Player2: ")
    players = [x_player, o_player]
    print(f"\nHello {players[0]} and {players[1]}!\nLet's play Tic Tac Toe!\n")

    return players

board = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}

used_field = [] # This will hold all fields already used

#used_field.append()

# the board
def print_board():
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

def choise(players):
    input(print(players[0] + "! Choose a field on the board"))
    input(print(players[1] + "! Choose a field on the board"))


players = newgame()
print_board()
choise(players)