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
# game_mode = get_user_level()
# print(game_mode) #checking if the above works and it does...

# creates game that selects random word from list and asks user for guesses
def mystery_game_easy(word_file):
    """Comp selects word 4-6 characters long and user guesses letter until word is complete or they run out of guesses"""
    with open(word_file) as file:
        words = file.read()
        file.close
    # create list of words from txt file of words
    list_words = []
    for word in words.split():
        if len(word) >= 4 and len(word) <= 6:
            list_words.append(word)
            
    return list_words
    
easy_words = mystery_game_easy("words.txt")
    


    # print instructions for user
    # print("You have a word that is 4-6 characters in length. You have 8 attempts to guess letters in the word.")
    # set variable to get guesses from user, store that letter.
    # get_guesses = input("Enter a letter:")
    # while 
# def normal_mode():

# def hard_mode():
