# Write a program that collects two stirngs from a user, inserts
# them into the string "Yesterday I wrote a [response_one]. I sent
# it to [response_two]!" and prints a new string.


response_one = input("What did you write? ")
response_two = input("Who did you send it to? ")

new_string = "Yesterday I wrote a {}. I sent it to {}!".format(response_one,response_two)

print(new_string)

