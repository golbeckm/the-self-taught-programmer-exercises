# Write a function that takes two objects
# as parameters and returns True if they
# are the same object, and False if not.

def compare(object_1, object_2):

    if object_1 == object_2:
        return True
    else:
        return False

result_1 = compare('Tom', 'Tim')
print(result_1)

result_2 = compare('Tim', 'Tim')
print(result_2)
