import random

dice_one = 1
dice_two = 10

player_input = input("Roll the dice? (y/n): ")


def dice_roler():
    random_num = random.randint(dice_one, dice_two)
    print(random_num, random.randint(dice_one, dice_two))


while player_input not in ("n", "N"):  # Exit the loop if ('n', 'N') in the input.
    if player_input not in ("y", "Y"):
        print("invalid input.")  # Invalid input if ('y', 'Y') is not in the input.
    else:
        dice_roler()  # Roll the dice if it's Y/y
    player_input = input(
        "Roll the dice? (y/n): "
    )  # Ask every time the user input to update the player_input to prvent the unwanted behaiver or infinite loop.

print("Thanks for playing.")
