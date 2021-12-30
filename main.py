from words import word_list
from ascii_art import art
import random
import platform
import os

# checks your OS and clears the terminal screen
def clear_console():
    system = platform.system()
    if system == "Linux" or system == "Darwin":
        os.system('clear')
    else:
        os.system('cls')

# Main Program
def main():
    # Change if exception info is needed
    debug_mode = 0
    try:
        # Initial assignments
        win = False
        attempts = 10
        score = 0
        word = word_list[random.randint(0, len(word_list))]
        hidden_word = '_ ' * len(word)
        guessed_letters = []

        # Actual game
        while attempts > 0:
            clear_console()
            print(art[10 - attempts])
            print(f"You have guessed: {guessed_letters}")
            print(f"You have {attempts} guesses left!")
            print(hidden_word)
            inputted = input()
            guessed_letters.append(inputted)

            # Checks if the inputted letter is inside the word
            if inputted in word:
                list_hidden = list(hidden_word)
                list_word = list(word)
                indexes = [index for index, element in enumerate(list_word) if element == inputted]

                # If the inputted letter is a duplicate letter in the string it will replace all
                # indexes where the letter appears - not just the first one
                for index_num in indexes:
                    list_hidden[((index_num + 1) * 2) - 2] = inputted
                hidden_word = ''.join(list_hidden)
                score += 1
                # Win check - probably a more efficient way to do this but this works well enough
                if score == len(word):
                    print(f"You won in {10 - attempts} guesses!\nThe word was: {word}")
                    win = True
                    break
            else:
                attempts -= 1

        if win is True:
            input()
        else:
            clear_console()
            print(art[10])
            print(f"You died, the word was {word}")

    except Exception as x:
        print("error occurred")
        if debug_mode == 1:
            print(x)

if __name__ == "__main__":
    main()
else:
    raise Exception("Standalone application - must not be imported as it is not a module")