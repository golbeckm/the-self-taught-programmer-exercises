# Find a file on your computer and print its contents using Python.

import os

filepath = os.path.join(os.sep, "Users", "golbeckm", "Desktop", "AISES", "Test.txt")

with open(filepath, "r") as file:
    print(file.read())
