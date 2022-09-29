# Prompt the user for their age. Convert it to a number, add one to it, 
# and tell them how old they will be on their next birthday.


age = int(input("How old are you? "))
birthday_next_year = age + 1
print(f"On your next birthday, your age will be {birthday_next_year}.")

print()

# print(f"On your next birthday, your age will be {age + 1}.")

#Prompt the user for the number of egg cartons they have. 
# Assume each carton holds 12 eggs, multiply their number by 12, and display the total number of eggs.

egg_cartons = int(input("How many egg cartons do you have? "))
total_eggs = egg_cartons * 12
print(f"You have: {total_eggs}")

# Prompt the user for a number of cookies and a number of people. Then, divide the number of cookies by the number of people to determine how many cookies each person gets.

print()

cookies = int(input("How many cookies do you have? "))
people = int(input("How many people are there? "))
print(f"Each person may have {cookies / people} cookies.")