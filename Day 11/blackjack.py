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

def text(final):
    print(f"  Your final hand: {player_deck}, final score: {sum(player_deck)}")
    print(f"  Computer's final hand: {opponent_deck}, final score: {sum(opponent_deck)}")
    print(final)

def opponent_win():
    text("You went over. You lose =(")

def player_win():
    text("Opponent went over. You win =)")

def drawn():
    text("This is a Drawn!")

def verify_pontuation(player1: list, player2: list):
    """Verify one of those two players win."""
    player_1 = sum(player1)
    player_2 = sum(player2)
    p_1 = player_1 > player_2
    p_2 = player_2 > player_1

    # Verify if the player_1 has a bad hand or the 21
    if player_1 > 21:
        return False
    elif player_1 == 21:
        return True

    # After the verify all those conditions, now is time to verify if the player_1.
    elif p_1 or p_2:
        another_card = input("Another card? (y/n): ").lower()

        if another_card != "y":
            if p_1:
                return True
            elif p_2:
                return False
        else:
            add_card(player_deck)
            table()

    # Verify if the two players has the same card count
    elif player_1 == player_2:
        return "Drawn"

def start():
    """Start the blackjack game."""
    # Show the logo
    print(logo)
    print("\n" * 50)

    # Set your deck and the opponent deck and start the table
    deck(player_deck)
    deck(opponent_deck)
    # while sum(opponent_deck) < 21:
    # add_card(opponent_deck)
    table()
    
    while True:
        winner = verify_pontuation(player_deck, opponent_deck)
        if winner == False:
            opponent_win()
            break
        elif winner == True:
            player_win()
            break
        elif winner == "Drawn":
            drawn()
            break

while True:
    confirm = input("Do you want to play a game of blackjack? (y/n): ")
    if confirm != "n":
        start()
        player_deck = []
        opponent_deck = []
    else:
        break