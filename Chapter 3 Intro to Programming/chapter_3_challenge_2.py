# write a program that prints a message if a variable is less than 10,
# and different message if the variable is less than or equal to 10.

variable = int(input("Enter a number: "))

if variable < 10:
    print(variable, "is less than 10")
elif variable > 10:
    print(variable, "is greater than 10")
