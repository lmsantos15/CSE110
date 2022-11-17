# 10 Prepare: Preparation Material

# I. ACCESSING ITEMS IN A LIST VIA THEIR INDEX
"You can access an item in a list at a given index via the square bracket [] notation:"
print()

first = the_list[0] # gets the first item
second = the_list[1] # gets the second item

index = int(input("Which index would you like to get? "))
user_choice = the_list[index] # gets the item at the index the user typed
"Don't forget that Python, like most programming languages, starts counting at 0 for its indexes. So the first item is at index 0, and the last item in a list of 10 elements would be at index 9."

# II. FINDING THE SIZE OF THE LIST
"You can find out how many elements are in a list, by using the len function (which is short for length) as follows:"
number_of_books = len(books)

# III. ITERATING THROUGH A LIST USING AN INDEX
"In previous lessons, you learned how to iterate through each item in a list using a standard for loop. Another way to do this is to have the loop iterate through the indexes 0 through the size of the list, and then access each item using the [] notation:"
for i in range(len(books)):
    book = books[i]
    print(book) # print each book to the screen
"Looking a little closer at that for loop you can see that len(books) gets the number of items in the list, and then the for i in range(...): part iterates through the numbers 0, 1, 2, 3, ..., up until (but not including) the size of the list. So if the list has 10 elements, this will loop through from 0–9, which are the exact indexes you want."

# IV. PRINTING INDEXES
"If you want to print the index numbers next to the elements of the list as you iterate through, you can print the value of the i variable:"

for i in range(len(books)):
    book = books[i]
    print(f" {i}. {book}")
"But be careful. Don't forget that the indexes will start at 0. If you want to display these numbers in a more user-friendly manner, you may need to add 1 to the variable i when you display it."

# V. WORKING WITH PARALLEL LISTS
"If you want to iterate through and display the name and the phone number, you would not be able to use a standard loop such as for name in names: because you wouldn't be able to get the corresponding number."
names = []
numbers = []

for i in range(len(names)):
    name = names[i]
    number = numbers[i]

    print(f"{name} - {number}")
# Keep in mind that you have to be very careful in cases like this that the two lists do not get out of sync.

# VI. REMOVING ITEMS FROM A LIST
"use the 'pop' function to pop the item out of the list. You tell the pop function the index of the item you want to remove. If you don't give it an index, it will remove the last one."
the_list.pop(3) # removes the item at index 3
the_list.pop() # removes the last item

"When you remove an item from a certain index, all of the elements in the list that follow it will move up. In other words, if you remove the item at index 3, the item that was at index 4 will move to 3, the one at 5 will move to 4, and so on."











