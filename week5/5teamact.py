# 05 Teach: Team Activity
# Grade Calculator

"""
A >= 90
B >= 80
C >= 70
D >= 60
F < 60
"""

# Empty String - To initialize an empty string in Python, 
# Just create a variable and don't assign any character or even no space. 
# This means assigning “” to a variable to initialize an empty string.
print()
# I. Core Requirements
grade = int(input("Enter you grade here: "))

letter = ""

if grade >= 90:
    letter = "A"
   
elif grade >= 80:
        letter = "B"

elif grade >= 70:
    letter = "C"

elif grade >= 60:
    letter = "D"

else:
    letter = "F"

print()
if grade >= 70:
    print("Amazing! You passed! \n")


# II. Stretch Challenge

# Challenge 01
# Add to your code the ability to include a "+" or "-" next to the letter grade, such as B+ or A-.
the_last_digit = grade % 10
sign = ""

if the_last_digit >= 7:
    sign = "+"
elif the_last_digit < 3:
    sign = "-"
else:
    sign = ""

# Challenge 02
# Recognize that there is no A+ grade, only A and A-. Add some additional logic to your program to detect this case and handle it correctly.

if grade >= 93:
    sign = ""

# Challenge 03
# Similarly, recognize that there is no F+ or F- grades, only F. Add additional logic to your program to detect these cases and handle them correctly.

if letter == "F":
    sign = ""


print(f"Your grade in letter is {letter}{sign}")

print("Education is the passport to the future, for tomorrow belongs to those who prepare for it today.")
print("by Malcolm X")


