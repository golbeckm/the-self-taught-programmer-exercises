# Take the list ["The", "fox", "jumped", "over", "the", "fence", "."]
# and turn it into a grammtically correct string. There should be a
# space between each word, but no space between the word fence and
# the period that follows it. (Don't forget, you learned a method
# that turns a list of strings into a single string

lst = ["The", "fox", "jumped", "over", "the", "fence", "."]

sentence = " ".join(lst)

end_result = sentence[0:-2]+"."

print(end_result)
