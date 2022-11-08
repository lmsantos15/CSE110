# 09 Prepare: Preparation Material

# Avoid using list as your variable name like this: list = [] # BAD EXAMPLE
"Once you have a list variables, you can add items to it using the append function. Notice that when you use it, you'll need to use parentheses () afterward, just like when we have called other functions like print and input."

# II. ADDING ITEMS TO A LIST

# Example:
# books = []

# books.append("1 Nephi")
# books.append("2 Nephi")
# books.append("Jacob")
# books.append("Enos")

# III. ITERATING THROUGH EACH ITEM IN A LIST

# print("Your books are:")

# for book in books:
    # print(book)

# IV. WORKING WITH LISTS OF NUMBERS
"When you have a list of numbers, a common task is to want to find the sum of all of these numbers or the largest number, or the smallest, etc. One strategy to accomplish this is to declare a variable outside a loop that you can reference in the loop as you iterate through each individual item."
# Example:
# receipts = [12.24, 18.50, 4.99, 21.75]

# running_total = 0

# for receipt in receipts:
  #  running_total = running_total + receipt

# Display the total
# print(f"The total is: {running_total:.2f}") # This displays: The total is: 57.48

# A new operator
# As you saw in the previous example, we can add to a variable with code like this:

# Example:
# age = 30
# age = age + 1

# print(age) # This displays: 31

# But because this is so common, there is an operator that can do this in one step. This is done using the += operator:

# age = 30
# age += 1

# print(age) # This displays: 31
"These two versions do the same thing, but people generally prefer to use the += operator because it's simpler, easy to understand, and less prone to mistakes."

"With this in mind, the previous code example could be updated to be the following:"

# for receipt in receipts:
    # Note the use of the += operator here
   # running_total += receipt

   