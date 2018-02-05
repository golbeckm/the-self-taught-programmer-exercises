# Change the Sqaure class so that when you print a Square
# object, a message prints telling you the len of each of
# the four sides of the shape. For example, if you create a
# square with Square(29) and print it, Python should print
# 29 by 29 by 29 by 29. 

class Square():
    
    square_list = []

    def __init__(self, s):

        self.side = s
        self.square_list.append((self.side))

    def print_side(self):

        print(""" {} by {} by {} by {}
              """.format(self.side,self.side,self.side,self.side))

my_square = Square(29)

my_square.print_side()
