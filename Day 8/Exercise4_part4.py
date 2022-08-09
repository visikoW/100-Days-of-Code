alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbol = ['!', '?', '*', '%', '&', '#', '$', '@']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    selected = char

    # To alphabetic characters only
    if char in alphabet:
        selected = alphabet
    
    # To number characters only
    elif char in numbers:
        selected = numbers

    # To symbol characters only
    elif char in symbol:
        selected = symbol

    # For every variety
    position = selected.index(char)
    new_position = position + shift_amount
    if char not in alphabet and char not in numbers and char not in symbol:
        new_position = 0

    if new_position > len(selected):
        new_position %= len(selected)
    end_text += selected[new_position]

  print(f"Here's the {cipher_direction}d result: {end_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
from art import *
print(logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    #Try running the program and entering a shift number of 45.
    #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
    #Hint: Think about how you can use the modulus (%).
    if shift > len(alphabet):
        shift %= len(alphabet)

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    # Test to continue
    answer = input("Do you want to restart the cipher program? (y/n): ")
    if answer.lower() != "y":
        break
