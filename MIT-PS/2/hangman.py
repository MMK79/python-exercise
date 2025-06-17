# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()
word = choose_word(wordlist)

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    check_list = []
    for i in secret_word:
        if i in letters_guessed:
            check_list.append(True)
        else:
            check_list.append(False)
    if False in check_list:
        return False
    else:
        return True

def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    secret_word_l = list(secret_word)
    for i in range(len(secret_word_l)):
        if secret_word_l[i] not in letters_guessed:
            secret_word_l[i] = '*'
    return (str(secret_word_l))

def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    char = 'abcdefghijklmnopqrstuvwxyz'
    char_l = list(char)
    for i in letters_guessed:
        if i in char_l:
            char_l.remove(i)
    char = ''.join(char_l)
    return (char)

def hangman(secret_word, with_help=False):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    print(secret_word)
    count = 10

    # give initial 10 guess
    while count >= 0 and not has_player_won(secret_word, guess):
        print()
        print(f"Your secret word have {len(secret_word)} and you have total of {count} Guess chance")
        print(get_word_progress(secret_word, guess))
        guess_input = input("Guess a Character:")

        # Check Guess input
        while len(guess_input) > 1 or len(guess_input) == 0 or guess_input in guess or guess_input in '1234567890':
            if guess_input in '1234567890':
                print()
                print("These are Valid input character",get_available_letters(guess))
                print("You are playing word game not numb game!")
                guess_input = input("Enter Valid Char, if you want help type !:\n")
                print()

            # Check if user entering same character
            elif guess_input in guess:
                print()
                print(get_available_letters(guess))
                guess_input = input("You entered same character, enter different one from the list below: \n")
                print()

            # Check if user entering single character
            else:
                print()
                guess_input = input("Only Enter Single Character:")
                print()
        # Save previous progress to use it later for comparison
        prv_prog = get_word_progress(secret_word, guess)
        # Append the new user input
        guess.append(guess_input)
        # Save the new progress to compare it later
        new_prog = get_word_progress(secret_word, guess)
        print(guess)
        # If player didn't won already we start comparing the new result to previous result
        if not has_player_won(secret_word, guess):
            # If new_prog be same as prv_prog means that our user guess didn't made any progression so we subtract from their amount of guess
            if new_prog == prv_prog:
                # If user used wrong ovel we subtract 2
                if guess[-1] in 'aieou':
                    count -= 2
                # Enable Help option
                elif guess[-1] == '!':
                    secret_word_l = list(secret_word)
                    secret_word_new = []
                    if count < 3:
                        print("You can't use help")
                    else:
                        for i in secret_word_l:
                            if i in secret_word_new:
                                pass
                            else:
                                secret_word_new.append(i)
                        for i in secret_word_new:
                            if i in guess:
                                secret_word_new.remove(i)
                        print(random.choice(secret_word_new))
                        count -= 3
                        del guess[-1]
                # Else we subtract 1
                else:
                    count -= 1
        else:
            print("You Won!")


    if not has_player_won(secret_word, guess):
        print("Sorry you lost :(")
        start = int(input("Wanna start new game? if yes type 1, if not type 0.\n"))
        flag = True
        while flag:
            if start == 1:
                secret_word = choose_word(wordlist)
                guess.clear()
                flag = False
                return hangman(secret_word)
            elif start == 0:
                print(":(")
                flag = False
                return None
            else:
                start = int(input("only 1 and 0, if yes type 1, if not type 0.\n"))

guess = []


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = False
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    # pass
