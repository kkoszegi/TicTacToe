import os

def game_start():
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
    while True:
        try:
            field = int(input(f"{player}! Choose a field on the board (1-9): "))
        except ValueError:
            print("Please, enter a NUMBER, idiot!")
            continue
        if (1 <= field <= 9) and (board[field] == " "):
            return field
        else:
            print("Invalid value!")
            continue

def victory(player, board):  # parameter 1: dictionary, parameter 2: "x"/"o", return: none/"x"/"o"
    if player == players[0]:
        xo = "x"
    elif player == players[1]:
        xo = "o"
    victs = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
    for vict in victs:
        if board[vict[0]] == board[vict[1]] == board[vict[2]] == xo:
            print(f"The winner is {player}!")
            return False

def score(player, players, x_score, o_score):
    if player == players[0]:
        x_score += 1
    elif player == players[1]:
        o_score += 1
    return [x_score, o_score]

def print_score(current_score, players):  # param. 1 is the return of score() function, that is a list, param. 2 is the list of players
    if current_score[0] > current_score[1]:
        print(f"{players[0]} leads to {current_score[0]}-{current_score[1]}.")
    elif current_score[1] > current_score[0]:
        print(f"{players[1]} leads to {current_score[1]}-{current_score[0]}.")
    elif current_score[0] == current_score[1] != 0:
        print(f"The round is draw: {current_score[0]}-{current_score[1]}.")

def new_round():
    answer = input("Do you want to play a new round? (y/n) ")
    return answer

def winner(current_score, players):
    if current_score[0] > current_score[1]:
        print(f"The ABSOLUTE WINNER is {players[0]}!")
    elif current_score[1] > current_score[0]:
        print(f"The ABSOLUTE WINNER is {players[1]}!")
    elif current_score[0] == current_score[1] != 0:
        print(f"The match is draw!")


players = game_start()
player = players[0]
x_score = o_score = 0
answer = "y"
while answer == "y":
    board = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
    end_of_round = None
    print_board(board)
    while end_of_round == None:
        field = choise(player, board)
        board = board_modify(player, board, field)
        os.system('clear')
        print_board(board)
        end_of_round = victory(player, board)
        if end_of_round == None:
            player = change_player(player, players)
    current_score = score(player, players, x_score, o_score)
    x_score = current_score[0]
    o_score = current_score[1]
    print_score(current_score, players)
    answer = new_round()
    if answer == "y":
        player = change_player(player, players)
        os.system('clear')
    else:
        winner(current_score, players)
        print("Goodbye!")
