# Create a function that accepts a string as
# a parameter and prints it.

def print_string(entered_string):
    """
    Prints the string given
    :param entered_string: string.
    :return: N/A
    """
    print("String entered:", entered_string)
    return 0

try:
    entered_string = input("Enter a string: ")
    print_string(entered_string)
    
except(ValueError):
    print("Invalid Input.")
