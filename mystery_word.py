import random
import string
##### help me understand lambda in list comprehension ##########


def get_user_level():
    """Asks the user for their level preference until they answer in valid format, then returns that level"""
    print("""Let's play a game! I'll generate a secret word and you have to guess the letters.\nThere are three levels.\nEasy will have words 4-6 characters in length.\nNormal has words 6-8 characters.\nHard has words that are 8 characters or more.\n""")
# defining acceptable answers by user for level selection as variable VALID_MODE
    valid_mode = ["Easy", "Normal", "Hard"]
# setting initial LEVEL to false so loop  will run
    level = False
# loop that will ask user for level preference until they answer with valid selection
##### use in statement instead if difficulty-- in['easy', medium etc]
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

def list_generator(word_file):
    """Comp selects word 4-6 characters long and user guesses letter until word is complete or they run out of guesses"""
    with open(word_file) as file:
        words = file.read().upper()      
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
# print(selection_list) #checking here to see if list selection works and it does

def get_user_input():
    """Gets a guess from user and makes sure it is only one alpha letter"""
# don't totally understand how while True works... is it just always true??
    while True:
# gooood LORD did you know .upper takes an argument!? NOW I DO AFTER ALL          DAY
        user_input = input("Guess a letter in the mystery word: ").upper()
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

def play_game():
    """Play the word guessing game loop"""
# print instructions for user
    # print("You have a word that is 4-6 characters in length. You have 8 attempts to guess letters in the word.")
# mystery_word variable uses random function to select from list, stores in list format
    mystery_word = list(random.choice(selection_list))
# set variable to get guesses from user, store that letter.
    guess = []
    attempts = 0
    all_guesses = []
    underscores = "_"

    while mystery_word not in all_guesses and attempts < 8:
        # print(mystery_word, "mystery word") # testing if it works!
# printing message that explains how many turns remain
        print(f"""There are {8 - int(attempts)} turns remaining. 
        Each incorrect guess will deduct from your turns.""")
# setting guess variable to get user input from another function above
        guess = get_user_input()
# adds user guesses to list called all_guesses
        all_guesses += str(guess)
# creating variable below to contain changing display word letters/underscores
        display = display_word(mystery_word, all_guesses)
        respond_to_user(mystery_word, guess)
        print("Here are all of your guesses so far: ", '*'.join(all_guesses))
######### it took me forever to get the following syntax right. could not figure out how to add my guesses to a list!!! ahaha!!!!!
        if guess not in mystery_word:
            attempts += 1
        if attempts >= 8:
            return option_play_again()
        if underscores not in display:
            print("You have won the game!")
            return option_play_again()
            
# could not get the display word to work unless I did print() inside function
def display_word(word, guesses):
    """creates display output that shows blank spaces replaced by letters for all the correct guesses"""
    display = [letter if letter in guesses else "_" for letter in word]
    print('  '.join(display))
    return display

def option_play_again():
    """Asks user if they'd like to play again after winning or losing"""
    play_again = True
    while play_again == True:
        ask = input("Do you want to play again? It's pretttttty fun...(answer Y/N): ").upper()
        if ask == "Y":
            # play_again = True
            return play_game()

        else:
            play_again = False
            print("Ok have fun today!")
            return
        
game_mode = get_user_level()
selection_list = list_generator("words.txt")
play_game()
# assigns variable GAME_MODE to whatever the user selected
# print(game_mode) #checking if the above works and it does...
    