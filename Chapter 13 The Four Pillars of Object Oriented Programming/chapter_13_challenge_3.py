import math

class Shape(): # Parent Class

    def __init__(self):
        pass

    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape): # Child Class inherits Parent class what_am_i method

    def __init__(self, l, w):
        self.length = l
        self.width = w

class Square(Shape): # Child Class inherits Parent class what_am_i method
    
    def __init__(self, s):
        self.side = s

new_rectangle = Rectangle(2,4)

print("The rectangles length is {} and the width is {}".format(new_rectangle.length, new_rectangle.width))

new_rectangle.what_am_i()

new_square = Square(10)

print("The squares side length is", new_square.side)

new_square.what_am_i()

