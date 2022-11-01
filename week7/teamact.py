# 07 Teach: Team Activity
# Guess my number game

print()

import random

number = random.randint(1, 10)

# Variables
magic_number = int(input("What is the magic number? "))
guess_number = int(input("What is your guess? "))

# Looping the questions
while magic_number != number:
    if guess_number <= number:
        print()
        print("Higher")

        magic_number = int(input("What is the magic number? "))
        guess_number = int(input("What is your guess? "))

    elif guess_number >= magic_number:
        print()
        print("Lower")
    
        magic_number = int(input("What is the magic number? "))
        guess_number = int(input("What is your guess? "))

print()

print("You guess it right!")
print()