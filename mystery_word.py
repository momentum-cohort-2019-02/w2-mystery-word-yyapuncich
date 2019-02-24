import random
import string


def get_user_level():
    """Asks the user for their level preference until they answer in valid format, then returns that level"""
# defining acceptable answers by user for level selection as variable VALID_MODE
    valid_mode = ["Easy", "Normal", "Hard"]
# setting initial LEVEL to false so loop  will run
    level = False
# loop that will ask user for level preference until they answer with valid selection
##### use in statement instead if difficulty in['easy', medium etc]
    while level != True:
        answer = input("What level would you like to play? Easy, Normal, or Hard? ").capitalize()
        if answer in valid_mode:
            level = True
            return answer
        else:
            level = False
            print("Invalid selection, please try again") 
    ###### keeping my previous version of this below, I liked Clinton's version in class Friday more :) ##########
    # while answer is not valid_mode:
    #     answer = input("What level would you like to play? Easy, Normal, or Hard? ").capitalize()
    #     if answer == "Easy":
    #         user_mode_select = "Easy"
    #         return user_mode_select
    #     elif answer == "Normal":
    #         user_mode_select = "Normal"
    #         return user_mode_select
    #     elif answer == "Hard":
    #         user_mode_select = "Hard"
    #         return user_mode_select
    #     else:
    #         user_mode_select = "Invalid"
    #         print("Invalid selection, please try again") 
        # now return to first question and ask again for valid entry

# assigns variable GAME_MODE to whatever the user selected
game_mode = get_user_level()
# print(game_mode) #checking if the above works and it does...

# creates game that selects random word from list and asks user for guesses
def list_generator(word_file):
    """Comp selects word 4-6 characters long and user guesses letter until word is complete or they run out of guesses"""
    with open(word_file) as file:
        words = file.read()
    # create list of words from txt file of words
    # set it up to do normal and hard mode here too, if else statements
    if game_mode == "Easy":
        list_words = [word for word in words.split() if (len(word) >= 4 and len(word) <= 6)]
        return list_words
    if game_mode == "Normal":
        list_words = [word for word in words.split() if (len(word) >= 7 and len(word) <= 8)]
        return list_words
    if game_mode == "Hard":
        list_words = [word for word in words.split() if (len(word) > 8)]
        return list_words

selection_list = list_generator("words.txt")
# print(selection_list) #checking here to see if list selection works and it does
def get_user_input():
    """Gets a guess from user and makes sure it is only one alpha letter"""
# don't totally understand how while True works... is it just always true??
    while True:
        user_input = input("Guess a letter in the mystery word: ")
        if user_input in list(string.ascii_letters):
            guess = str(user_input)
            if len(guess) == 1:     
                return guess
        
        print("Invalid entry, please enter only one letter and try again!")          

def respond_to_user(mystery_word, guess):  
    if guess in list(mystery_word):        
        print("Correct")
    else:
        print("Try again!")

            # output = 


def play_game():
    """Play the word guessing game loop"""
    # print instructions for user
    print("You have a word that is 4-6 characters in length. You have 8 attempts to guess letters in the word.")
    # set variable to get guesses from user, store that letter.
    mystery_word = list(random.choice(selection_list))
    guess = None
    attempts = 0
    all_guesses = []
    
    # print(display_list) # testing if it works!
    while guess != mystery_word and attempts < 8:
        # print(mystery_word) # testing if it works!
        guess = get_user_input()
        respond_to_user(mystery_word, guess)
        attempts += 1
         ######### it took me forever to get the following syntax right. could not figure out how to add my guesses to a list!!! ahaha!!!!!
        all_guesses += str(guess)
        print_word(mystery_word, all_guesses)
        # print(all_guesses) # testing if list of guesses works and. it. does.
        print(f"""This was attempt number {attempts}. You have 8 total attempts. Would you like to play again?""")

def display_word(word, guesses):
    display = [letter if letter in guesses else "_" for letter in word]
    return display

def print_word(word, guesses):
    output_letters = [display_word(letter, guesses) for letter in word]
    print(output_letters)
            
    #get user input Y/N and let them play again or thank them for playing

play_game()   
    