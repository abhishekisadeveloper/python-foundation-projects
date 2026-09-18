import random


def guess(x):
    random_number = random.randint(1, x) # computer gnrt.
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess the random number betweem 1 to {x} ")) # user input
        if guess > random_number:
            print("sorry, this is too high.")
        elif guess < random_number:
            print("sorry, this is too low.")

    print(
        f"wwooohhhooo, You got this congratulations..... this is your random number {random_number}"
    )


guess(20)
