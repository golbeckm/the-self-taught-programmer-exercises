# Write a program that asks a user a question, and saves their answer to a file.

import os

filepath = os.path.join(os.sep, "Users", "golbeckm", "Desktop", "AISES", "Color.txt")

with open(filepath, "w+") as file:
    color = input("What is your favorite color? ")
    file.write(color)

