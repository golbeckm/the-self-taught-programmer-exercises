# Write a function that takes three required parsmeters
# and two optional parameters.

def sum_of_five_numbers(num_1, num_2, num_3, num_4 = 2, num_5 = 8):
    """
    Returns the sum of 5 numbers.
    :param num_1: int.
    :param num_2: int.
    :param num_3: int.
    :param num_4: int.
    :param num_5: int.
    :return: int sum of five numbers
    """
    result = num_1 + num_2 + num_3 + num_4 + num_5
    print("Sum of", num_1, "+", num_2, "+", num_3, "+", num_4, "+", num_5, "is", result)
    return 0

try:
    print("Enter three numbers as follows...")
    num_1 = int(input("Enter the first number: "))
    num_2 = int(input("Enter the second number: "))
    num_3 = int(input("Enter the third number: "))
    print("Now we will sum them with 2 and 8 as the fourth and fifth number....")
    sum_of_five_numbers(num_1, num_2, num_3)
    
except(ValueError):
    print("Invalid Input.")
