# 07 Prepare: Checkpoint

# Assignment

# 1
# Use a while loop to ask the user for a positive number (>= 0). Continue asking as long as the number is negative, then display the number.

print()
number = float(input("Please type a positive number: "))

while number < 0:
    print("Sorry, that is a negative number. Please try again.")
    number = int(input("Please type a positive number: "))
print()
print(f"The number is: {number}.")
print()

# 2
# Use a while loop, to simulate a child asking their parent for a piece of candy. Have the program keep looping until the user answers "yes", then have the program output "Thank you.



candy = str(input("May I have a piece of candy? "))


while candy.lower() != "yes":
    candy = str(input("May I have a piece of candy? "))
    
print()
print("Thank you for your candy.")
print()



