# Write a function that converts a string to a float and returns the result.
# Use exception handling to catch the exception that could occur.

def convert_string_to_float(entered_string):
    
    try:
        result = float(entered_string)
        return result
    
    except(ValueError):
        print("Invalid Input")
        exit

entered_string = input("Enter a number: ")

result = convert_string_to_float(entered_string)

print("End result:",result)
        
        
