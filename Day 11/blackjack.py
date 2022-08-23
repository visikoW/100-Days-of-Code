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

def end_game():
    # Verify if the player just passed the number of cards necessary to play again.
    def player_win():
        print(f"  Your final hand: {player_deck}, final score: {sum(player_deck)}")
        print(f"  Computer's final hand: {opponent_deck}, final score: {sum(opponent_deck)}")
        print("You went over. You lose =(")
    def opponent_win():
        print(f"  Your final hand: {player_deck}, final score: {sum(player_deck)}")
        print(f"  The computer's final hand: {opponent_deck}, final score: {sum(opponent_deck)}")
        print("Opponent went over. You win =)")

def start():
    """Start the blackjack game."""
    # Space and show the logo
    print("\n" * 50)
    print(logo)

    # Set your deck and the opponent deck and start the table
    deck(player_deck)
    deck(opponent_deck)
    while sum(opponent_deck) < 21:
        add_card(opponent_deck)
    table()

    # Play
    while True:
        # Who will win?
        # First Try: The player start with the good hand?
        # Second Try: Your hand overpass the limit?
        if sum(player_deck) == 21 or sum(player_deck) > 21:
            end_game()
            break

        # Third Try: The hand isn't enoght to end the game?
        elif sum(player_deck) < 21:
            again = input("Type 'y' to get another card, type 'n' to pass: ")
            if again == "y":
                add_card(player_deck)
                table()
            else:
                end_game()
                break

while True:
    confirm = input("Do you want to play a game of blackjack? (y/n): ")
    if confirm != "n":
        start()
        player_deck = []
        opponent_deck = []
    else:
        break