# Write a program that lets the user ask your height, favorite
# color, or favorite anime, and returns the result from the
# dictionary in the prevouis challenge.

height = input("What is your height? ")
favorite_color = input("What is your favorite color? ")
favorite_anime = input("What is your favorite anime? ")

my_favorites = dict()
my_favorites['Height:'] = height
my_favorites['Favorite Color:'] = favorite_color
my_favorites['Favorite Anime:'] = favorite_anime

print(my_favorites)
