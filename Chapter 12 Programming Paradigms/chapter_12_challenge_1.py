class Apple():

    def __init__(self, c, t, a, e):
        self.color = c
        self.taste = t
        self.age = a
        self.expirationDate = e

green_apple = Apple("green", "sour", "5 days old", "10-25-2017")

print("The apples color is", green_apple.color)
print("The apples taste is", green_apple.taste)
print("The apples age is", green_apple.age)
print("The apples expiration date is", green_apple.expirationDate)
