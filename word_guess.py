"""File Name: word_guess.py
Author: W. Henry Bateman
Date Completed: 10/20/2023

Description: THis CLI game prompts player 1 enter a secret word and a number of guesses allowed
player 2 then guesses letters in the secret word. If player 2 runs out of tries, player 1 wins.
if player 2 guesses all the letters within the number of tries, player 2 wins.
"""


def main():
    # Start program loop
    p1_score = 0
    p2_score = 0
    
    play_again = True
    while play_again == True:
        # To keep track of num tries and decrement when guess incorrect
        num_tries = 0
        # To keep track of correct guesses
        correct_guesses = ""
        # Bool for controlling game loop
        game_is_over = False

        # Get secret word
        secret_word = safely_get_secret_word()

        # Get num tries
        num_tries = safely_get_num_tries()

        # Start game loop
        while game_is_over == False:
            
            # Make a guess
            guess_char_token = False
            while guess_char_token == False:
                # Print num tries
                print(f"NUM TRIES: ({num_tries})\n")
                # Get guess letter
                secret_word_guess_input = get_guess_char()
                # If input passes check
                if guess_input_check(secret_word_guess_input) == True:
                    guess_char_token = True
                    # Checks input for matches, stores string of correct matches
                    did_guess_correct = check_for_matches_and_return_correct_letters(guess_char = secret_word_guess_input,
                                                                secret_word = secret_word, 
                                                                guesses = correct_guesses)
                    # If there are some correct guesses
                    if len(did_guess_correct) != 0:
                        # Increment string of correct guesses
                        correct_guesses += did_guess_correct
                        if len(correct_guesses) == len(secret_word):
                            print("\n\n~~~[PLAYER 2] WINS!~~~\n")
                            p2_score += 1
                            # Print player scores
                            print(f"[PLAYER 1]: ({p1_score}) | [PLAYER 2]: ({p2_score})\n")
                            # End game loop
                            game_is_over = True
                    else:
                        # Decrement num tries
                        num_tries -= 1
                        # If out of tries game over
                        if num_tries == 0:
                            print("\n\n~~~[PLAYER 1] WINS!~~~\n")
                            p1_score += 1
                            # Print player scores
                            print(f"[PLAYER 1]: ({p1_score}) | [PLAYER 2]: ({p2_score})\n")
                            # End game loop
                            game_is_over = True
        
        play_again = play_again_prompt()

    print("\n\n[END OF PROGRAM]\n\n")
    

#-----------------------------------------END OF MAIN--------------------------------------------#
    

# Get Input Functions
def safely_get_secret_word() -> str:
    """This func keeps prompting for secret word if input is invalid, returns the secret word"""
    word_input_check_token = False
    while word_input_check_token == False:
        secret_word = get_Secret_Word()
        if secret_word_input_Check(secret_word) == True:
            return secret_word
        else:
            word_input_check_token = False    


def get_Secret_Word() -> str:
    """This function prompts Player 1 to enter the secret word and returns that string"""
    
    secret_word = input("\n[PLAYER 1] ENTER SECRET WORD: ")
    return secret_word


def safely_get_num_tries() -> int:
    """This func keeps asking for num tries if the input is invalid, returns the number of tries as int"""
    num_tries_input_token = False
    while num_tries_input_token == False:
        num_tries_input = get_num_tries_input()
        if num_tries_input_check(num_tries_input) == True:
            return int(num_tries_input)
        else:
            num_tries_input_token = False


def get_num_tries_input() -> str:
    """This func prompts player 1 to enter an integer for how many guesses player 2 will receive"""

    num_tries = input("\n[PLAYER 1] ENTER NUMBER OF TRIES: ")
    return num_tries


def get_guess_char() -> str:
    """This function gets the guess letter from player 2 and returns it as a string"""

    guess_char = input("\n[PLAYER 2] GUESS A LETTER: ")
    return guess_char


def play_again_prompt() -> bool:
    """This function prompts the user to choose whether or not to end the game and returns a bool accordingly"""

    inputCheckToken = False
    while inputCheckToken == False:
        end_code_input = input("\nPLAY AGAIN? (1)YES (2)NO\n")
        if end_code_input.isnumeric() == True and len(end_code_input) == 1:
            if int(end_code_input) == 1:
                return True
            if int(end_code_input) == 2:
                return False
            else:
                inputCheckToken = False
                print("INVALID INPUT")
        else:
            inputCheckToken = False
            print("INVALID INPUT")


#------------------------------------------------------------------------------------------#


# Display secret word functions
def check_for_matches_and_return_correct_letters(guess_char: str, secret_word: str, guesses: list) -> str:
    """This func checks to see if the currently guessed char is in the secret word and prints/returns
     the letters that have been correctly guessed """

    correct_substring = ""
    for i in range(len(secret_word)):
        if guess_char == secret_word[i]:
            print(f"{guess_char}", end = " ")
            correct_substring += guess_char
        else:
            if secret_word[i] in guesses:
                print(f"{secret_word[i]}", end = " ")
            if secret_word[i] not in guesses:
                print("_", end = " ")

    if guess_char in secret_word:
        print("\nYES, GOOD GUESS")
    else:
        print("\nNOPE, TRY AGAIN")
    return correct_substring

#------------------------------------------------------------------------------------------#
            

# Input check functions
def secret_word_input_Check(inputToCheck: str) -> bool:
    """This func takes in the secret word string from get_secret_word and 
    makes sure it is a word containing only alphabetic characters"""

    if inputToCheck.isalpha() == True:
        return True
    else:
        return False
    
    
def num_tries_input_check(inputToCheck: str) -> bool:
    """This func checks in the input is numeric and returns a bool accordingly"""
    if inputToCheck.isnumeric() == True:
        return True
    else:
        return False

    
def guess_input_check(inputToCheck: str) -> bool:
    """This func takes the guess input from get_guess and returns a bool whether the
    character is valid or not"""

    if inputToCheck.isalpha() == True:
        return True
    if len(inputToCheck) > 1:
        return False
    else:
        return False
    

# Call main function to run program
main()







