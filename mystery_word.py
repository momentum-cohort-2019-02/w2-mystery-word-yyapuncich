import random
import string

# Ask user what mode to play in
user_mode_select = input("What level would you like to play? Easy, Normal, or Hard? ")

# check if mode is valid
def check_mode(mode):
    user_mode_select = user_mode_select.capitalize()
    if user_mode_select != "Easy" or "Normal" or "Hard":
        print("invalid selection, please enter valid level: ")



