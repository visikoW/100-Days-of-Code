import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

# Creating the map for rock paper and scissors to help find the choose_number
map = [rock, paper, scissors]

# Selecting the RPS
choose_number = int(input("That do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

# Telling to the player who're his enemy, and what's his choice
against = random.randint(0, 2)

# Checking if everything is ok to continuate.
if choose_number > 2 or choose_number < 0:  # If the number is much bigger than expected, you shall lose
    print("You typed an invalid number, you lose!")
else:
    # Printing the choices
    print(map[choose_number])  # Player choice
    print("Computer chose: \n" + map[against])  # Computer choice

    # saying if you win or lose the game

    win = ("You win")
    lose = ("You lose")

    if choose_number == 0 and against == 2:  # Else If your choice is Rock and the against is Scissors, you win
        print(win)
    elif choose_number == 2 and against == 0:  # Else If your choice is Scissors and the against is Rock, you lose
        print(lose)
    elif choose_number > against:  # For conditionals: 1 -> 0 and 2 -> 1
        print(win)
    elif choose_number < against:  # For conditionals: 0 -> 1 and 1 -> 2
        print(lose)
    elif choose_number == against:  # If those 2 players use the same object, them draw.
        print("It's a draw")
