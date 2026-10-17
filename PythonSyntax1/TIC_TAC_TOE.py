# Tic-Tac-Toe Game
board = [" " for _ in range(9)]

def display_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def make_move(player, position):

    if board[position] == " ":
        board[position] = player
        return True
    return False

def isWinner(player):

    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    for combo in winning_combinations:
        if (board[combo[0]] == player and
            board[combo[1]] == player and
            board[combo[2]] == player):
            return True

    return False

def is_board_full():

    return " " not in board

current_player = "X"

while True:
    display_board()

    try:
        position = int(input(f"Player {current_player}, enter position (1-9): ")) - 1

        if position < 0 or position > 8:
            print("Invalid position! Choose 1 to 9.")
            continue

        if not make_move(current_player, position):
            print("Position already occupied!")
            continue

        if isWinner(current_player):
            display_board()
            print(f"🎉 Player {current_player} Wins!")
            break

        if is_board_full():
            display_board()
            print("🤝 It's a Draw!")
            break

        # Switch Player
        current_player = "O" if current_player == "X" else "X"

    except ValueError:
        print("Please enter a valid number.")