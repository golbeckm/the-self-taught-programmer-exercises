# Write a program with a variable age assigned to an
# integer that prints different strings depending
# on what integer age is

age = int(input("Enter your age: "))

if age <= 5:
    print("You are a baby.")
elif age > 5 and age < 13:
    print("You are a kid.")
elif age >= 13 and age < 16:
    print("You are a teenager.")
elif age >= 16:
    print("You are a adult.")
else:
    print("Not a real number.")
