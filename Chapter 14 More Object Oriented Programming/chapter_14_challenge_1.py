# Add a square_list class variable to a class called
# Square so that every time you create a new Square
# object, the new object gets added to the list.

class Square():
    
    square_list = []

    def __init__(self, s):

        self.side = s
        self.square_list.append((self.side))

s1 = Square(5)
s2 = Square(10)
s3 = Square(15)

print(Square.square_list)

