import math

class Circle():

    def __init__(self, r):
        self.radius = r

    def Area(self):
        return (math.pi*(math.pow(self.radius, 2)))

new_circle = Circle(5)

print("The circles radius is", new_circle.radius)
print("The circles area is", round(new_circle.Area(), 2))

