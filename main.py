from random import randint

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

players = {
    "players_one": "X",
    "players_two": "O",
    "current_player": "",
    "winner_player": "",
}


def display_board():
    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
    print("----------")
    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
    print("----------")
    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")


def get_starter():
    """Return a random starting player among two players"""
    random_n = randint(0, 1)
    if random_n == 0:
        players["current_player"] = players["players_one"]
    else:
        players["current_player"] = players["players_two"]


def switch_round():
    """Alternate round among two players"""
    if players["current_player"] == "O":
        players["current_player"] = players["players_one"]
    else:
        players["current_player"] = players["players_two"]


def assign_symbol(row, column):
    """Assign the player's symbol to the user chosen field"""
    for _ in board:
        board[row][column] = players["current_player"]


def check_for_rows():
    """Check for rows winning combinations and return the winner player"""
    if board[0][0] == board[0][1] == board[0][2] == players["current_player"] or \
            board[1][0] == board[1][1] == board[1][2] == players["current_player"] \
            or board[2][0] == board[2][1] == board[2][2] == players["current_player"]:
        players["winner_player"] = players["current_player"]
        # print(f"{players['winner_player']}, You win!")
        return players["winner_player"]


def check_for_columns():
    """Check for columns winning combinations and return the winner player"""
    if board[0][0] == board[1][0] == board[2][0] == players["current_player"] or \
            board[0][1] == board[1][1] == board[2][1] == players["current_player"] \
            or board[0][2] == board[1][2] == board[2][2] == players["current_player"]:
        players["winner_player"] = players["current_player"]
        # print(f"{players['winner_player']}, You win!")
        return players["winner_player"]


def check_for_diagonals():
    """Check for diagonals winning combinations and return the winner player"""
    if board[0][0] == board[1][1] == board[2][2] == players["current_player"] or \
            board[0][2] == board[1][1] == board[2][0] == players["current_player"]:
        players["winner_player"] = players["current_player"]
        # print(f"{players['winner_player']}, You win!")
        return players["winner_player"]


def is_winning():
    """Return True if there is a winning combination and display winning message"""
    if check_for_rows() or check_for_columns() or check_for_diagonals():
        display_board()
        print(f"{players['winner_player']}, You win!")
        return True


def board_is_full():
    """Take count of the number of assigned fields and returns True when board is full"""
    number_assigned_fields = 0
    for row in board:
        for x in row:
            if x == players["players_one"] or x == players["players_two"]:
                number_assigned_fields += 1

    if number_assigned_fields == 9:
        display_board()
        print("It's a tie!")
        return True


def game():
    get_starter()
    shall_continue = True
    while shall_continue:

        print("********************************************")
        print(f"It's {players['current_player']} turn\n")
        display_board()

        user_row = int(input("Type the number of the row: 1, 2 or 3?\n")) - 1
        user_column = int(input("Type the number of the column: 1, 2 or 3?\n")) - 1

        assign_symbol(user_row, user_column)

        if is_winning() or board_is_full():
            shall_continue = False
        else:
            switch_round()


game()
