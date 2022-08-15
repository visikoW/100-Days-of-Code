def clear():
    print("\n" * 50)

clear()

from art import *
print(logo)

def find_hightest_bidder(bidder_record):
    higgest = 0
    winner = ""
    for bidder in bidder_record:
        bidder_amount = bidder_record[bidder]
        if bidder_amount > higgest:
            higgest = bidder_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${higgest}")

bids = {}
while True:
    name = input("What's your name? ")
    price = input("What's your bid? ")

    bids[name] = int(price)

    test = input("Are there any other bidders? (y/n): ")

    if test == "n":
        find_hightest_bidder(bids)
        break
    clear()
