# 09 Prove: Assignment Milestone

import math

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

print("\n Please select one of the following: ")
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
        print()
        price = int(input("How much is the price? "))

        list_of_items.append(item)
        list_of_items_price.append(price)

        print()
        print(f" '{item}' has been added to your cart.")

    elif action == 2:
        print()
        print("The contents of your shopping cart are: ")

        for shop in range(len(list_of_items)):
            print(f"{shop + 1} {list_of_items[shop]} - ${list_of_items_price[shop]: .2f}")


    elif action == 3:
        print()
        item_remove = int(input("Which item would you like to remove? "))

        del list_of_items[item_remove - 1]
        del list_of_items_price[item_remove - 1]
        print()
        print("Item removed.")

    elif action == 4:
        print()
        total_price = math.fsum(list_of_items_price)
        print(f"The total price of the items in the shopping cart are ${format(total_price,'.2f')}")

        print()

    print("Please select one of the following: \n1. Add item \n2. View cart \n3. Remove item \n4. Compute total \n5. Quit \n")

    action = int(input("Please enter an action: "))
    print()

    
print("Thank you for shopping with us!")

print()