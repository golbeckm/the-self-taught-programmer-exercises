import math

class Rectangle():

    def __init__(self, l, w):
        self.length = l
        self.width = w

    def calculate_perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return (round(perimeter, 2))

class Square():
    
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return (round((4 * self.side), 2))

new_rectangle = Rectangle(2,4)

print("The rectangles length is {} and the width is {}".format(new_rectangle.length, new_rectangle.width))
print("The rectangles perimeter is", round(new_rectangle.calculate_perimeter(), 2))

new_square = Square(10)

print("The squares side length is", new_square.side)
print("The squares perimeter is", round(new_square.calculate_perimeter(), 2))
