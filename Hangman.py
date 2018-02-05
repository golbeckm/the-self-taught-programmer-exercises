# Classic hangman game
import random

def hangman(word):
    wrong_guesses = 0
    stages = ["",
              " ___________           ",
              "|           |          ",
              "|           |          ",
              "|           O          ",
              "|          /|\         ",
              "|          / \         ",
              "|_____________________ "
              ]
    remaining_letters = list(word)
    letter_board = ["___"] * len(word)
    win = False
    print("Welcome to Hangman!!!")
    while wrong_guesses < len(stages) - 1:
        message = "\nGuess a letter "
        guess = input(message)
        if guess in remaining_letters:
            character_index = remaining_letters.index(guess)
            letter_board[character_index] = guess
            remaining_letters[character_index] = '$'
        else:
            wrong_guesses += 1
        print((" ".join(letter_board)))
        print("\n".join(stages[0:wrong_guesses + 1]))
        if "___" not in letter_board:
            print("You Win!!!")
            print("".join(letter_board), "was the word.")
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong_guesses]))
        print("You lose!! The word was {}.".format(word))

words = ["cat", "pokemon", "magic", "python", "time", "germany"]
word_choice = random.choice(words)
hangman(word_choice)

