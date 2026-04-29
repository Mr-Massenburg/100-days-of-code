# Day 12 | Number Guessing Game - Scope and Constants

import random
from art import logo

EASY_LIVES = 10
HARD_LIVES = 5

def check_guess(player_guess, answer, turns):
    """Checks the users guess and removes one turn if incorrect"""
    if player_guess > answer:
        print("Too high.")
        return turns -1
    elif player_guess < answer:
        print("Too low.")
        return turns - 1
    elif player_guess == answer:
        print(f"You got it! The answer was {answer}")
        return turns

def set_difficulty():
    """Based on user input assigns the number of lives the user gets"""
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_LIVES
    elif difficulty == "hard":
        return HARD_LIVES

def number_guessing_game():
    """Main game function"""
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    lives = set_difficulty()
    # Selects the random number between 1 and 100
    the_number = random.randint(1, 100)
    
    # print(the_number) # Line used to debug and test while programming

    guess = 0

    while guess != the_number:
        # Displays number of lives remaining
        print(f"You have {lives} attempts remaining to guess the number.")
        # Takes in users guess
        guess = int(input("Make a guess: "))

        # Checks if user guessed correctly, if not, subtracts 1 from the number of lives
        lives = check_guess(guess, the_number, lives)

        # Informs user they have run out of lives and that the game is over
        if lives == 0:
            print("You've run out of guesses. Refresh game to try again.")
            return
        elif guess != the_number:
            print("Guess again.")

number_guessing_game()
