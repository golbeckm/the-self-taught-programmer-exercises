
# This is an example of composition. Composition models the "has a"
# relationship by storing an object as a variable in another object.
# This example is the relationship between a horse and its rider.


class Horse():
    def __init__(self,
                 name,
                 breed,
                 rider):
        self.name = name
        self.breed = breed
        self.rider = rider

class Rider():
    def __init__(self, name):
        self.name = name

red = Rider("Red Pollard")
seabiscuit = Horse("Seabiscuit",
                   "Stallion",
                   red)

print(seabiscuit.rider.name)
