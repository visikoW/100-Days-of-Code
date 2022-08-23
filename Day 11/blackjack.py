############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_deck = []
opponent_deck = []

def table():
    """Table of cards for each player."""
    print(f"  Your cards: {player_deck}, current score: {sum(player_deck)}")
    print(f"  Computer's first card: {opponent_deck[0]}")

def add_card(player: list):
    """Add a new card on the current deck."""
    player.append(random.choice(cards))

def deck(player: list):
    """Define the deck for a player, need to define the first argument as a list."""
    for x in range(0,2):
        add_card(player)

# Verify if the player just passed the number of cards necessary to play again.
def opponent_win():
    print(f"  Your final hand: {player_deck}, final score: {sum(player_deck)}")
    print(f"  Computer's final hand: {opponent_deck}, final score: {sum(opponent_deck)}")
    print("You went over. You lose =(")

def player_win():
    print(f"  Your final hand: {player_deck}, final score: {sum(player_deck)}")
    print(f"  The computer's final hand: {opponent_deck}, final score: {sum(opponent_deck)}")
    print("Opponent went over. You win =)")

# End Game
def end_game(player_decision):
    """Tell if the player or the opponent win"""
    sum_player = sum(player_deck)
    sum_opponent = sum(opponent_deck)

    if sum_player == sum_opponent:
        return print("Drawn")
    elif sum_player == 21:
        return player_win()
    elif sum_player > 21:
        return opponent_win()
    elif sum_opponent > 21:
        return player_win()
    elif sum_opponent == 21:
        return opponent_win()

    if player_decision == "y":
        add_card(player_deck)

    if sum_opponent > sum_player:
        return opponent_win()
    elif sum_player > sum_opponent:
        return player_win()

def start():
    """Start the blackjack game."""
    # Show the logo
    print(logo)
    print("\n" * 50)

    # Set your deck and the opponent deck and start the table
    deck(player_deck)
    deck(opponent_deck)
    while sum(opponent_deck) < 21:
        add_card(opponent_deck)
    table()

    while True:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        end_game(another_card)

while True:
    confirm = input("Do you want to play a game of blackjack? (y/n): ")
    if confirm != "n":
        start()
        player_deck = []
        opponent_deck = []
    else:
        break