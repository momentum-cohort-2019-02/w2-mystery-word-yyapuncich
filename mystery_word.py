import random
import string

# defining acceptable answers by user for level selection as variable VALID_MODE
valid_mode = "Easy" or "Normal" or "Hard"

def get_user_level():
    """Asks the user for their level preference until they answer in valid format, then returns that level"""
    # assigning variable ASK to empty string before question is asked
    ask = ""
# loop that will ask user for level preference until they answer with valid selection
    while ask is not valid_mode:
        ask = input("What level would you like to play? Easy, Normal, or Hard? ").capitalize()
        if ask == "Easy":
            user_mode_select = "Easy"
            return user_mode_select
        elif ask == "Normal":
            user_mode_select = "Normal"
            return user_mode_select
        elif ask == "Hard":
            user_mode_select = "Hard"
            return user_mode_select
        else:
            user_mode_select = "Invalid"
            print("Invalid selection, please try again") 
        # now return to first question and ask again for valid entry

# assigns variable GAME_MODE to whatever the user selected
game_mode = get_user_level()
# print(game_mode) #checking if the above works and it does...

# def normal_mode():

# def hard_mode():



# easy_mode(user_mode_select)