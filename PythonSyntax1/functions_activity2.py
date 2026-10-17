
import random

# Function to move a car
def move_car():
    return random.randint(1, 3)

# Function to display the race track
def show_race(player, computer):
    print("\nPlayer : " + "-" * player + "🏎️")
    print("Computer: " + "-" * computer + "🚗")

# Function to check the winner
def check_winner(player, computer):
    if player >= 20:
        return "Player"
    elif computer >= 20:
        return "Computer"
    return None

# Main function
def play_game():
    player = 0
    computer = 0

    print("🏁 Welcome to the Python Racing Game!")
    print("First to reach 20 wins.\n")

    while True:
        input("Press Enter to race...")

        player += move_car()
        computer += move_car()

        show_race(player, computer)

        winner = check_winner(player, computer)

        if winner:
            print(f"\n{winner} wins the race!")
            break

# Start the game
play_game()

# import random

# # Function 1: Move the car
# def move_car():
#     # Return a random number between 1 and 3
#     __________


# # Function 2: Display the race
# def show_race(player, computer):
#     print("\nPlayer : " + "-" * player + "🏎️")
#     print("Computer: " + "-" * computer + "🚗")


# # Function 3: Check who has won
# def check_winner(player, computer):
#     if __________:
#         return "Player"
#     elif __________:
#         return "Computer"
#     else:
#         return __________


# # Function 4: Main game
# def play_game():
#     player = 0
#     computer = 0

#     print("🏁 Welcome to the Python Racing Game!")
#     print("First to reach 20 wins!")

#     while __________:
#         input("Press Enter to race...")

#         player = player + __________
#         computer = computer + __________

#         show_race(__________, __________)

#         winner = check_winner(__________, __________)

#         if winner:
#             print(winner, "wins the race! 🎉")
#             __________


# # Start the game
# play_game()
