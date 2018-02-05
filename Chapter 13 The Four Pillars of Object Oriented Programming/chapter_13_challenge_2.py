import math

class Square():
    
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return (round((4 * self.side), 2))

    def change_size(self, change):
        if (self.side + change > 0):
            self.side = (self.side + change)
        else:
            print("Cant make the sides less than 0. Please try again.")
            

new_square = Square(10)

print("The squares side length is", new_square.side)
print("The squares perimeter is", round(new_square.calculate_perimeter(), 2))

print("Now lets decrease each side by 15.")

new_square.change_size(-15)

print("Now lets decrease each side by 5.")

new_square.change_size(-5)

print("The squares side length is", new_square.side)
print("The squares perimeter is", round(new_square.calculate_perimeter(), 2))

print("Now lets increase each side by 15.")

new_square.change_size(15)

print("The squares side length is", new_square.side)
print("The squares perimeter is", round(new_square.calculate_perimeter(), 2))



