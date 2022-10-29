# 07 Teach: Team Activity
# Guess my number game

import random
print()


# # Core Requirements

# # 01
# magic_number = random.randint(1, 10)
# guess = -1

# if guess != magic_number:
#     guess = int(input("What is your guess? "))

#     if guess < magic_number:
#         print("Higher :)")
#         guess = int(input("What is your guess? "))

#     elif guess > magic_number:
#         print("Lower :)")
#         guess = int(input("What is your guess? "))

# else:
#     print("You guessed it!")
# I am stock on this part. Was about to use loop, but it says "At this point you won't have any loops."
# Hoping I understood the instruction correctly.
print()

# 02
# Add a loop that keeps looping as long as the guess does not match the magic number.

print()

magic_number = random.randint(1, 10)
guess = ""

if guess == magic_number:
    guess = int(input("What is the magic number? "))
    print("You guessed it!")

    while guess < magic_number:
        guess = int(input("What is the magic number? "))
        print("Higher")

    



