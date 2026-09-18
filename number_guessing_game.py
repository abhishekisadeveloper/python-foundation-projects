import random

MIN_RANGE = 1
MAX_RANGE = 100


def comp_number():
    computer_guess = random.randint(MIN_RANGE, MAX_RANGE)
    return computer_guess


computer = comp_number()
while True:
    try:
        user_guess = int(input(f"Guess the Number from {MIN_RANGE} to {MAX_RANGE}: "))

        if computer > user_guess:
            print("Too low!")
        elif computer < user_guess:
            print("Too high!")
        else:
            print("congrats! you have guess it right!")
            break
    except ValueError:
        print("Invalid input!")
