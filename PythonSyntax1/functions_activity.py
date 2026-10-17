import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def find_winner(player, computer):
    if player == computer:
        return "Draw"

    if player == "rock" and computer == "scissors":
        return "Player"
    elif player == "paper" and computer == "rock":
        return "Player"
    elif player == "scissors" and computer == "paper":
        return "Player"
    else:
        return "Computer"


def play_game():
    player = input("Enter rock, paper or scissors: ")

    computer = get_computer_choice()

    print("Computer chose:", computer)

    winner = find_winner(player, computer)

    print("Winner:", winner)


play_game()