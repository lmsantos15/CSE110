# 08 Teach: Team Activity
# Iterating Through Strings


# III. STRETCH CHALLENGE

# Start a new program that will work similar to one from the core requirements, but use a different string, this time using the following quote from President Nelson: "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."

# Then, instead of your program asking for a favorite letter, have it asks for a number n. Make the program capitalize every n-th letter in the string.
print()
qoute = "President Russell M. Nelson: In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."

continue_running = "yes"

while continue_running == "yes":
    number = int(input("Please enter a number: "))

    for i, letter in enumerate(qoute):
        if i % number == 0:
            print(letter.upper(), end="")

        else:
            print(letter.lower(), end="")

    print()
    continue_running = input("Would you like to enter another number? ")

print()
print("Have a nice day. Goodbye!")

"Had to follow the same structure as the one in the sample solution. Looking forward on being independent and not relying much on others sample solution in the future."
