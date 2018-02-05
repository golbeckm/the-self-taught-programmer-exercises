# Write a program with two functions. The first function should take an integer
# as a parameter and return the result of the integer divided by 2. The second
# function should take an integer as a parameter and return the result of the
# integer multiplied by 4. Call the first function, save the result as a variable,
# and pass it as a parameter to the second function.

def divide_by_2(user_int):
    """
    Returns the result of a number divided by 2
    :param user_int: int.
    :return: result of dividing user_int by 2
    """
    return user_int / 2

def multiply_by_4(user_int):
    """
    Returns the result of a number multiplied by 4
    :param user_int: int.
    :return: result of multipling user_int by 4
    """
    return user_int * 4

try:
    user_int = int(input("Enter an integer: "))
    result = divide_by_2(user_int)
    end_result = multiply_by_4(result)
    print("End result is", end_result)

except(ValueError):
    print("Invalid Input")
    
