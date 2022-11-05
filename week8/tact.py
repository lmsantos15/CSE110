# 08 Teach: Team Activity
# Iterating Through Strings

print()
# CORE REQUIREMENTS

magic_word = "commitment"

favorite_letter = input("What is your favorite letter? ")

# II. CORE REQUIREMENTS
# 1 and 2

# 1 Create a string variable to hold the word "Commitment".

# Write code that loops through the word letter by letter. If the letter is "m", print it as a capital letter. If the letter is # anything else, print it out as a lowercase letter.

# For this part, it is ok to print each letter on it's own line.

# 2 Change the print statements so that each letter is not printed on its own line, but rather they are printed out next to each other on the same line.

# Also, change the program to allow the user to specify the letter (rather than always using "m"). Make sure your program matches the letter in the word, regardless of whether the user entered it as a capital or lowercase, and regardless of whether that letter was a capital or lowercase in the original word.
for letter in magic_word:

    if letter.lower() == favorite_letter.lower():
        print(letter.upper(), end="")

    else:
        print(letter.upper(), end="")

print()

# 3
# Change the program, so that instead of capitalizing the user's favorite letter, it "hides" it, and replaces it with an  underscore in the display.

for letter in magic_word:

    if letter.lower() == favorite_letter.lower():
        print("_", end="")
    
    else:
        print(letter.lower(), end="")

print()
