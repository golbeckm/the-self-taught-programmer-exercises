import math

class Hexagon():

    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return (round((6 * self.side), 2))

new_hexagon = Hexagon(5)

print("The hexagons side length is", new_hexagon.side)
print("The hexagons perimeter is", round(new_hexagon.calculate_perimeter(), 2))
