# 10 Prepare: Checkpoint

"Ask the user for a list of list of items in a shopping list, stop asking for items when the user types 'quit.'"

print()

print("Please enter the items of the shopping list (Type: quit to finish):")

"Loop through the items in the regular way (for example, for thing in the_list) and display each one to make sure you have the initial list built correctly."
shopping_list = []
item = ""

while item != "quit":
    item = input("Item: ")

    if item != "quit":
        shopping_list.append(item)

print()

"Add another loop to go through and print the items in the list, but this time, instead of using the for ... in syntax, use an index (for example, for ... in range) and then access the item using the index and the square brackets. Print the index in front of the items like so: 0. Milk"

print("The shopping list is: ")
for item in shopping_list:
    print(item)

print()
print("The shopping list with indexes is: ")
for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(f"{i}. {item}")

print()

index = input("Which item would you like to change? ")
new_item = input("What is the new item? ")

shopping_list[i] = new_item

print()
print("The shopping list with indexes is:")
for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(f"{i}. {item}")

print()

"Ask the user for an index and a new shopping list item. Replace the item at that index with the new item. Then, display the whole list again."




