# 09 Prove: Assignment Milestone

# Project Description"
"For this project you will create a program that stores a list of products in a shopping cart along with their prices. The user should have the ability to add items to the list, remove them, and see the total price of the cart."

print()

print("Welcome to the Shopping Cart Program!")

# Milestone Requirements 1, 2, 5

# I. ADD A NEW ITEM
# II. DISPLAY THE CONTENTS OF THE SHOPPING CART
# V. QUIT

list_of_items = []
list_of_items_price = []

action = ""

print()

print("Please select one of the following: ")
print()
print("1. Add item")
print("2. View cart")
print("3. Remove item")
print("4. Compute total")
print("5. Quit")

print()

while action != 5:

    if action == 1:
        print()
        item = input("What is the item would you like to add? ")

        list_of_items.append(item)
        print()
        print(f" '{item}' has been added to your cart.")

    elif action == 2:
        print()
        print("The contents of your shopping cart are: ")

        for list_items in list_of_items:
            print(list_items)

    elif action == 3:
        print()

    elif action == 4:
        print()

    action = int(input("Please enter an action: "))

print("Thank you for shopping with us!")

print()