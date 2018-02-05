import math

class Triangle():

    def __init__(self, b, h):
        self.base = b
        self.height = h

    def Area(self):
        return (round((.5 * self.base * self.height), 2))

new_triangle = Triangle(5, 10)

print("The triangles base is", new_triangle.base)
print("The triangles heaight is", new_triangle.height)
print("The triangles area is", round(new_triangle.Area(), 2))
