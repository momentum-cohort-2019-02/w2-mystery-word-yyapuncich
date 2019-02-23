import random
import string

# defining acceptable answers by user for level selection as variable VALID_MODE
valid_mode = "Easy" or "Normal" or "Hard"
def get_user_level():
    """Asks the user for their level preference until they answer in valid format, then returns that level"""
    # assigning variable ASK to empty string before question is asked
    answer = ""
# loop that will ask user for level preference until they answer with valid selection
##### use in statement instead if difficulty in['easy', medium etc]
    while answer is not valid_mode:
        answer = input("What level would you like to play? Easy, Normal, or Hard? ").capitalize()
        if answer == "Easy":
            user_mode_select = "Easy"
            return user_mode_select
        elif answer == "Normal":
            user_mode_select = "Normal"
            return user_mode_select
        elif answer == "Hard":
            user_mode_select = "Hard"
            return user_mode_select
        else:
            user_mode_select = "Invalid"
            print("Invalid selection, please try again") 
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
   
def play_game():
    """Play the word guessing game loop"""
    # print instructions for user
    print("You have a word that is 4-6 characters in length. You have 8 attempts to guess letters in the word.")
    # set variable to get guesses from user, store that letter.
    guess = input("Enter a letter:")
    mystery_word = random.choice(selection_list)
    while guess != mystery_word:
        guess = get_user_input()
        respond_to_user(mystery_word, guess)
        attempts += 1

    print(f"This was attempt number {attempts}. You have 8 total attempts")

play_game()