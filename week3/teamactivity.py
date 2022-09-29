# # 03 Teach: Team Activity

print("Square")
print()
length_side = float(input("What is the length of a side of the square? "))
area = length_side ** 2
print(f"The are of the square is: {area}")
print()

print("Rectangle")

print()
length = float(input("What is the length of rectangle? "))
width = float(input("What is the width of the rectangle? "))
area2 = length * width
print(f"The area of the rectangle is: {area2}")

print()

print("Circle")

print()
radius = float(input("What is the radius of the circle? "))
area10 = 3.14 * (radius ** 2)
print(f"The area of the circle is: {area10}")
print()
print()
print()
print()
print("Stretch Challenge")
print()
# Stretch 1
from collections.abc import Sized
import math
radius2 = float(input("What is the radius of the circle? "))
area3 = math.pi * (radius2 ** 2)
print(f"The area of the circle is: {area3}")
print()
print()
print()
# Stretch 2
# Value
value = float(input("What is the value to be used? "))
# Calculating areas
area_square = value ** 2
area_circle = math.pi ** 3
volume_cube = value ** 3
volume_sphere = (4 / 3) * math.pi * (value ** 3)

# Displaying the results

print(f"Area of a square: {area_square}")
print(f"Area of a circle: {area_circle}")
print(f"Volume of a cube: {volume_cube}")
print(f"Volume of a sphere: {volume_sphere}")
print()
print()
print()

# Stretch 3
# Square
side = float(input("What is the length of a side of the square (cm)? "))
area5 = side ** 2

print(f"The area of the square is: {area5} cm^2")
print(f"The area of the square is: {area5 / 10000} m^2")
print()
print()
print()
# Area of a rectangle
length6 = float(input("What is the length of rectangle (cm)? "))
width6 = float(input("What is the width of the rectangle (cm)? "))
area6 = length6 * width6
print(f"The area of the rectangle is: {area6} cm^2")
print(f"The area of the rectangle is: {area6 / 10000} m^2")
print()
print()
print()
# Area of Circle
radius8 = float(input("What is the radius of the circle (in cm)? "))
area8 = 3.14 * (radius8 ** 2)
print(f"The area of the circle is: {area8} cm^2")
print(f"The area of the circle is: {area8 / 10000} m^2")
# We had to copy mosto f the code since we were lost on how we can start
# Personal note: I was able to slowly understand the purpost of STR, INT, and FLOAT
# Still a bit confused, but I am slowly getting it :)
# Thanks



