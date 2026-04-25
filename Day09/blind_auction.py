# Day 9 | Blind Auction - Dictionaries

from os import system
from art import logo

def find_highest_bid(auction_dict):
    winner = max(auction_dict, key=auction_dict.get)
    print(f"The winner is {winner} with a bid of ${auction_dict[winner]}.")


print(logo)
print("Welcome to the secret auction program.")

auction_data = {}
auction_is_open = True

while auction_is_open:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    auction_data[name] = bid

    more_bids = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if more_bids == "yes":
        system("clear")
        continue
    else:
        auction_is_open = False
        find_highest_bid(auction_data)



