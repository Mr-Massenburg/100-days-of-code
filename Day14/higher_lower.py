# Day 14 | Higher Lower Game

from art import logo, vs
from game_data import data
import random
from os import system

def get_choice():
    """Returns a random selection from the available game data"""
    return random.choice(data)

def check_answer(user_guess, cpu_a, cpu_b):
    """Returns True if user choice was correct and False it not"""
    if user_guess == 'A':
        if cpu_a['follower_count'] > cpu_b['follower_count']:
            return True
        elif cpu_a['follower_count'] < cpu_b['follower_count']:
            return False
    elif user_guess == 'B':
        if cpu_b['follower_count'] > cpu_a['follower_count']:
            return True
        elif cpu_b['follower_count'] < cpu_a['follower_count']:
            return False

def game():
    """Main game function"""
    score = 0
    guess_is_correct = True
    option_a = get_choice()

    while guess_is_correct:
        system("clear")
        print(logo)
        if score > 0:
            print(f"You're Right! Current score: {score}.")

        #Display Option A and B for the user to pick from
        print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}.")

        print(vs)

        option_b = get_choice()

        print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}.")

        #Prompt user for their guess
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        player_selected = {}

        if guess == 'A':
            player_selected = option_a
        elif guess == 'B':
            player_selected = option_b

        guess_is_correct = check_answer(guess, option_a, option_b)

        if guess_is_correct:
            option_a = player_selected
            score += 1

    system("clear")
    print(logo)
    print(f"Sorry, that's wrong. Final Score: {score}")

game()
