# Write a program with an infinite loop (with the option to type q to quit)
# and a list of numbers. Each time through the loop ask the user to guess a
# number on the list and tell them whether or not they guessed correctly.
import random

number_list = [25, 45, 40, 88]

while True:
    guess = input("Guess a number or type q to quit. ")
    if guess == "q":
        break
    try:
        guess = int(guess)
    except ValueError:
        print("Please type a number or q to quit.")
    if guess in number_list:
        print("You guessed correctly!!", guess, "is in the list")
    else:
        print("You guessed wrong. Please try again.")
