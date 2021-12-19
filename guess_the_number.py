# Author: H J Poe
# This program will allow the user to guess a number between 1 and 10. 

import random

rand = random.randint(1, 10)
guesses = 0

# The following function tests a string to see if it is an integer.


def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


print("I'm thinking of a number between 1 and 10.")

# Ask the user for a guess and validate it.
guess = input("What do you think it is?")
while represents_int(guess) is not True:
    guess = input("That is not a valid number.")

# If the user is correct on their first guess, let
# them know they got it right.
if int(guess) == rand:
    print("Yay! You got it!")

# Ask the user to guess again until they get the correct answer.
while int(guess) != rand:
    # If the user's guess is too low:
    if int(guess) < rand:
        guesses += 1
        guess = int(input("Too low! Guess again:"))
        # Validate the new guess.
        while represents_int(guess) is not True:
            guess = input("That is not a valid number.")
    else:
        # If the user's guess is to high:
        if int(guess) > rand:
            guesses += 1
            guess = int(input("Too high! Guess again:"))
            # Validate the new guess.
            while represents_int(guess) is not True:
                guess = input("That is not a valid number.")
    # Tell the user when they get the answer right.
    if int(guess) == rand:
        print("Yay! You got it!")
        print("Guesses: ", guesses)
