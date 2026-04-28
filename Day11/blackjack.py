#Day 11 | Blackjack - Capstone Project

import random
from os import system
from art import logo

def deal_card():
    """Returns a random card from the deck"""
    return random.choice(cards)

def calculate_score(hand):
    """Calculates the score of the hand its given. Checks hand for ace if score over 21"""
    score = sum(hand)
    if score > 21 and 11 in hand:
        ace_position = hand.index(11)
        hand[ace_position] = 1
        score = sum(hand)
    return score

def win_check(player1):
    """Checks if player has 21 or busts"""
    if player1 >= 21:
        return True
    else:
        return False

def win_conditions(p1, cpu):
    if p1 == cpu:
        print("It's a tie.")
    elif p1 == 21:
        print("You win with Blackjack!")
    elif p1 > 21:
        print("You went over. You Lose.")
    elif cpu == 21:
        print("You lose. Dealer has Blackjack.")
    elif cpu > 21:
        print("Opponent went over. You win!")
    elif cpu > p1:
        print("You lose.")
    elif p1 > cpu:
        print("You win!")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

game_running = True
while game_running:
    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if start_game == 'y':
        system("clear")
        # system("cls") # This line would clear the screen on a Windows machine. I use MacOS.
        print(logo)

        player_hand = []
        cpu_hand = []

        player_score = 0
        cpu_score = 0

        for num in range(2):
            player_hand.append(deal_card())
            cpu_hand.append(deal_card())

        players_turn = True
        win_or_bust = False

        while players_turn:
            player_score = calculate_score(player_hand)
            cpu_score = calculate_score(cpu_hand)

            print(f"Your cards: {player_hand}, current score: {player_score}")
            # print(cpu_hand) # Line was used to show the cpu's hand for testing while programming
            print(f"Computer's first card: {cpu_hand[0]}")

            if win_check(player_score):
                win_or_bust = True
                break

            hit_or_pass = input("Type 'y' to get another card, type 'n' to pass: ").lower()

            if hit_or_pass == 'y':
                player_hand.append(deal_card())
            elif hit_or_pass == 'n':
                players_turn = False

        while cpu_score < 17 and not win_or_bust:
            cpu_hand.append(deal_card())
            cpu_score = calculate_score(cpu_hand)


        print(f"Your final hand: {player_hand}, final score: {player_score}")
        print(f"Computer's final hand: {cpu_hand}, final score: {cpu_score}")
        win_conditions(p1=player_score, cpu=cpu_score)

    else:
        game_running = False
