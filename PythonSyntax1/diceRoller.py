import random

def roll_dice():
    return random.randint(1, 6)

def play_game():
    print("🎲 Dice Game")

    player = roll_dice()
    computer = roll_dice()

    print("Player rolled:", player)
    print("Computer rolled:", computer)

    if player > computer:
        print("🎉 Player wins!")
    elif computer > player:
        print("🤖 Computer wins!")
    else:
        print("It's a draw!")

play_game()
