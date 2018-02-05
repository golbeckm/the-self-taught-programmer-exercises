# write a program that prints a message if a variable is less than or eual to 10,
# another messae if the variable is greater than 10 but less than or equal to 25,
# and anothe rmessage if the variable is greater than 25. 

variable = int(input("Enter a number: "))

if variable <= 10:
    print(variable, "is less than or equal to 10")
elif variable > 10 and variable <= 25:
    print(variable, "is greater than 10 but less than or equal to 25")
elif variable > 25:
    print(variable, "is greater than 25")
