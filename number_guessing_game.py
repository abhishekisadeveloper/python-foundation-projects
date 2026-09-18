# we have user and computer, as a player
# computer generate random num one time. from x to y and pic one.
# Loop here.
# take user input & compair it with the computer num.
#   if guess > comp_num print guess again, it's too high.
#   elif guess < comp_num print too low
#   else print congrats! you have guess it right.


import random

MAX_RANGE = 1
MIN_RANGE = 100

def comp_number():
    computer_guess = random.randint(MAX_RANGE, MIN_RANGE)
    print(computer_guess)
    return computer_guess

# comp_number() runing 2 times, but we need only ones.

user_guess = None

computer = comp_number()
while True:
    user_guess = int(input(f'Guess the Number from {MIN_RANGE} to {MAX_RANGE}: '))
    if computer > user_guess:
        print('sorry this is too low!')
    elif computer < user_guess:
        print('sorry this is too high gess!')
    else:
        print('congrats! you have guess it right!')
    
        
    print(user_guess)