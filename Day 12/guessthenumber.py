#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import *
import random

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
CHOOSE = input("Choose a dificulty. Type 'easy' or 'hard': ").lower()
RANDOM_NUMBER = random.randint(0, 100)

def number_test(num):
    if num > RANDOM_NUMBER:
        return "Too high"
    elif num < RANDOM_NUMBER:
        return "Too Low."
    else:
        return True

def winner(result):
    if result == True:
        print(f"You got it! The answer was {RANDOM_NUMBER}.")
        return True
    else:
        print(result)
        print("Guess again.")

def start(attempts):
    ATTEMPTS = attempts
    while True:
        print(f"You have {ATTEMPTS} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        result = number_test(guess)
        test = winner(result)
        if test:
            break
        ATTEMPTS -= 1
        if ATTEMPTS == 0:
            print("You've run out of guesses, you lose.")
            break

if CHOOSE == 'easy':
    start(10)

elif CHOOSE == 'hard':
    start(5)
