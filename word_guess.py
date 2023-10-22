

def main():
    num_tries_possible = 0
    num_correct = 0
    num_incorrect = 0
    p1_score = 0
    p2_score = 0

    # Get secret word
    word_input_check_token = False
    while word_input_check_token == False:
        secret_word = get_Secret_Word()
        if secret_word_input_Check(secret_word) == True:
            break
        else:
            word_input_check_token = False

    # Get num tries
    num_tries_input_token = False
    while num_tries_input_token == False:
        num_tries_input = get_num_tries()
        if num_tries_input_check(num_tries_input) == True:
            # Set value for num_tries
            num_tries_possible = int(num_tries_input)
            break
        else:
            num_tries_input_token = False

    end_program_bool = False

    # BEGIN GAME SESSION
    while end_program_bool == False:

        # Get num tries
        inputCheckToken = False
        while inputCheckToken == False:
            num_tries = get_num_tries()
            if num_tries_input_check(num_tries) == True:
                break
            else:
                inputCheckToken = False

        # Get secret word
        secret_word_token = False
        while secret_word_token == False:
            secret_word_input = get_Secret_Word()
            if secret_word_input_Check(secret_word_input) == True:
                secret_word = secret_word_input
                break
            else:
                secret_word_token = False

        # Make a guess
        guess_char_token = False
        while guess_char_token == False:
            secret_word_guess_input = get_guess_char()
            if guess_input_check(secret_word_guess_input) == True:
                if secret_word_guess_input in secret_word:
                     pass
                     #TODO FINISH STUFF


        # Checks number of tries
        if num_incorrect == num_tries_possible:
            print("\n[PLAYER 1] WINS!!")
            p1_score += 1
            print(f"\n[PLAYER 1] SCORE: {p1_score}")
            get_end_code = end_game()
            if get_end_code == True:
                print("\n\n\nGOODBYE!\n~PROGRAM END~\n")
                exit()
            if get_end_code == False:
                end_program_bool = False

        # Checks number of correct letters
        if num_correct == len(secret_word):
            print("\n[PLAYER 2] WINS!!!")
            p2_score += 1
            print(f"\n[PLAYER 1] SCORE: {p2_score}")
            get_end_code = end_game()
            if get_end_code == True:
                print("\n\n\nGOODBYE!\n~PROGRAM END~\n")
                exit()
            if get_end_code == False:
                end_program_bool = False


#-----------------------------------------END OF MAIN--------------------------------------------#
    

# Get Input Functions
def get_Secret_Word() -> str:
    """This function prompts Player 1 to enter the secret word and returns that string"""
    
    secret_word = input("\n[PLAYER 1] ENTER SECRET WORD: ")
    return secret_word


def get_num_tries() -> str:
    """This func prompts player 1 to enter an integer for how many guesses player 2 will receive"""

    num_tries = input("\n[PLAYER 1] ENTER NUMBER OF TRIES: ")
    return num_tries


def get_guess_char() -> str:
    """This function gets the guess letter from player 2 and returns it as a string"""

    guess_char = input("\n[PLAYER 2] GUESS A LETTER: ")
    return guess_char

def end_game() -> bool:
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
    if int(inputToCheck) > 20:
        return False
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
    









