# # car_count = 100

print("II. USING FORMAT STRINGS")
print()
# # # The simplest way, was recently added to python, and that is to put an f right before your string, as shown:

# # print(f"There are at least {car_count} cars in Manila.")
# # print()
# # # Another approach is to not use the f before the string, but instead, use .format() after the string, as shown:

# # print("There are at least {} cars in Manila.".format(car_count))


# print()
# # In a format string, you define the precision, or number of decimals to display, by putting a :.2f after the variable name (changing the 2 to whichever amount you'd like).
print("III. FORMAT STRING OPTIONS")
print()
# vans = 5
# passenger = 55

# people_per_car = passenger / vans

# # Round to 1 decimal
# print(f"There are {people_per_car:.1f} people in the car.")

# # Round to 2 decimals
# print(f"There are {people_per_car:.2f} people in the car.")

# # Round to 3 decimals
# print(f"There are {people_per_car:.3f} people in the car.")

# # Scientific Notation
# # You can tell the computer to display the number in scientific notation, or "exponent" notation by using :.3e after your variable, where 3 defines the precision and e indicates that you are using exponent notation.
# print()
# distance = 11 * 2306 * 2.5

# # Scientific notation with 3 digits of precision
# print(f"The distance is {distance:.3e} meters.")

# # Scientific notation with 6 digits of precision
# print(f"The distance is {distance:.6e} meters.")
# print()
# # Thousand Grouping
# # When you write numbers in code, you don't use commas to separate the groupings of digits (in other words, you don't write: 10,000,000, just 10000000). Recently, Python added a notation that lets you type using underscores such as 10_000_000.

# # In any case, when you want to display large numbers to the user, you may want to display it with commas or underscores. This is done by using either :, or :_ after the variable name.

# big_number = 123124534

# # Display without formatting
# print(f"The number is: {big_number}")

# # Display with "," formatting
# print(f"The number is: {big_number:,}")

# # Display with "_" formatting
# print(f"The number is: {big_number:_}")

print("IV. USING THE MATH LIBRARY")
import math
print()

radius = 5
area = math.pi * (radius ** 2)
print(f"The are is {area}")





weight = 1.65

lower = math.floor(weight)
print(lower)
print()
higher = math.ceil(weight)
print(higher)

print("V. GOOD STYLE")
# Whenever you write a program, you need to be conscious of the fact that your program will need to be understood and potentially reused or modified by others in the future. It may be used by other people on your team, or future employees of the company, or it may simply be you returning to your program after a few months, trying to remember what you had done.