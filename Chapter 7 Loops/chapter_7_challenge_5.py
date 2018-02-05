# Multiply all the numbers in the list [8, 19, 148, 4] with all the numbers
# in the list [9, 1, 33, 83], and append each result to a third list.

first_list = [8, 19, 148, 4]
second_list = [9, 1, 33, 83]
multiplied = []

for i in first_list:
    for j in second_list:
        multiplied.append(i*j)

print(multiplied)

