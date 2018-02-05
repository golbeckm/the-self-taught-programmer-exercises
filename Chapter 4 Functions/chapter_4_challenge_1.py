# Write a function that takes a number as
# an input and returns that number squared.

def squared_num(num_1):
    """
    Returns a number squared
    :param num_1: int.
    :return: int square of number given
    """
    return num_1 ** 2

try:
    num_1 = int(input("Enter a number: "))
    result = squared_num(num_1)
    print("Result: ", result)
    
except(ValueError):
    print("Invalid Input.")

    
