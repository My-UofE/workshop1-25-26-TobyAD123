import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    x = random.choice(poss_values)   
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    if next_val < current_val:
        if user_input == "l":
            output = True
        else:
            output = False

    elif next_val > current_val:
        if user_input == "h":
            output = True
        else:
            output = False

    return output


# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    if letter not in word:
        print("Sorry", letter, "is not in the word")
        return False
    
    else:
        word_list = list(word)
        for i in range(len(word_list)):
            if word_list[i] == letter:
                board[i] = letter
        
        print("Well done!", letter, "is in the word")
        return True
