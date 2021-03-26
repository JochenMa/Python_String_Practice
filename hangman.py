"""
File: hangman.py
Name: Jo
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    The console will come out a random word from the random_word function
    The player has 7 turns to guess
    If the word is correct, the guess will be printed
    If not, the player will lose one turn, and the hangman picture will be printed
    If there is no turns, the player will lose
    """
    answers = random_word()
    turns = N_TURNS
    word = ''
    # To get the len of answer in to " _ "
    for i in range(len(answers)):
        word += '-'
    print("The word looks like: "+word, end="")
    print("")
    print("You have " + str(turns) + " guesses left.")
    # If the answer is not equal to the word, the player can keep guessing
    while answers != word:
        guess = input("Your guess: ")
        # Case-sensitive
        guess = guess.upper()
        # Avoid the player inputs wrong guess
        if not guess.isalpha():
            print('illegal format.')
        else:
            # If the guess is one of the letters
            if guess in answers:
                # To check all the letter in the answer, it will loop for the len of answer times
                for i in range(len(answers)):
                    # To place the guess into the word list
                    if answers[i] == guess:
                        word = word[:i] + guess + word[i + 1:]
                print("The word looks like: " + word, end="")
                print("")
                print("You have " + str(turns) + " guesses left.")
            else:
                # The case of wrong guessing, minus turns and draw the hangman
                turns = turns - 1
                if turns == 6:
                    print("_____")
                    print("|")
                    print("|")
                    print("|")
                    print("|")
                    print("|")
                    print("|")
                    print("|")
                    print("____________")
                if turns == 5:
                    print("_____")
                    print("|    |")
                    print("|")
                    print("|")
                    print("|")
                    print("|")
                    print("|")
                    print("|")
                    print("____________")
                if turns == 4:
                    print("_____")
                    print("|    |")
                    print("|  (   )")
                    print("|")
                    print("|")
                    print("|")
                    print("|")
                    print("|")
                    print("____________")
                if turns == 3:
                    print("_____")
                    print("|    |")
                    print("|  (   )")
                    print("|    |")
                    print("|    |")
                    print("|    |")
                    print("|")
                    print("|")
                    print("____________")
                if turns == 2:
                    print("_____")
                    print("|    |")
                    print("|  (   )")
                    print("|   /|\\")
                    print("|  / | \\")
                    print("|    |")
                    print("|")
                    print("|")
                    print("____________")
                if turns == 1:
                    print("_____")
                    print("|    |")
                    print("|  (   )")
                    print("|   /|\\")
                    print("|  / | \\")
                    print("|    |")
                    print("|   / \\")
                    print("|  /   \\")
                    print("____________")
                print('There is no ' + str(guess) + "'s in the word.")
                # When the player has no turns
                if turns == 0:
                    print("_____")
                    print("|    |")
                    print("| (X__X)")
                    print("|   /|\\")
                    print("|  / | \\")
                    print("|    |")
                    print("|   / \\")
                    print("|  /   \\")
                    print("____________")
                    print('You are completely hung : (')
                    print('The word was: ' + answers)
                    pass
                else:
                    print("The word looks like: "+word, end="")
                    print("")
                    print("You have " + str(turns) + " guesses left.")
    print('You win!!')
    print('The word was: ' + answers)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()