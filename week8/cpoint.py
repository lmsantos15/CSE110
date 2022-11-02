# 08 Prepare: Checkpoint


print()

# people = ["Mike" , "Jean"]

# FOR loop
# for name in people:
#      print(name)

# print()

# index = 0
# while index < len(people):
#     print(people[index])
#     index = index + 1

# print()

# I. LOOPING THROUGH A LIST

print()

# items = ["Ballpen", "Pencil", "Guitar", "TV", "Helmet", "Paper", "Wallet"]

# for items in items:
#     print(f"The item is: {items}")
# print()

# II. LOOPING THROUGH NUMBERS

# print()
# numbers = range(25)

# Without + 1 the range will end at 24

# for numbers in range(25 + 1):
#     print(numbers)

# This loop will start with 100, and go up to, but not including 200
# for i in range(100, 200):
#     print(i)

# This loop will do the same thing, but this time, it will count by 10's
# for i in range(100, 200, 10):
#     print(i)

# III. LOOPS WITHIN LOOPS

# for i in range(5 + 1):
#     print(i)


# print()

# for i in range (5 + 1):
#     print(i)
#     for j in range(10, 13):
#         print(f"---{j}")
print()
# We can add a second, inner loop, that for each one of those displays the numbers 10-12 (with two - characters in front to make it easier to visualize).
# Notice how the inner loop is run every time the outer loop displays it's number. Inner loops can be very helpful in iterating through a two-dimensional structure, such as the pixels in an image.

# Hint from Instructor:
"While we generally prefer variable names that are more descriptive than a single letter, if the variable will only be used for counting in a simple loop it is considered standard to use i. Then, if you have an inner loop, you use j, and a third inner loop would be k. If you have more than three loops you should consider if there is a simpler way to accomplish your task, and if there really isn't, you should at least move to more descriptive variable names at that point."



# IV. LOOPING THROUGH STRINGS
"You can iterate through each letter of a string using either style of for-loop. For example, you can loop through each letter one at a time with the following code:"

# first_name = "Mike and Jean"
# for letter in first_name:
#     print(f"The letter is: {letter}")
# print()

# Accessing Letters by Position
"Sometimes you need to access a letter by its position (or index) in a string. In other words, you might want to know the third or seventh letter in a string. This will be useful when comparing letters at the same place in two strings, such is in your project for this lesson."

"You can access a specific letter in a string by using the square brackets [], such as word[3] or word[12]. But be aware that that the count starts at 0, so you will use 3 to get the fourth letter (not the third letter). The following example gets the fourth letter of the name:"

# first_name = "Jeaneva"

# fourth_letter = first_name[5] # Notice, using 3 instead of 4
# print(fourth_letter) # outputs a 'g' on the screen


# Iterating through each letter using an index
"In the previous sections you learned how to iterate through each letter in a string, but this only gave you access to the letter but not the index of that letter. In many cases, this is sufficient. However, in other cases you need to know both the letter and its index. (For example, in your project you need to know the letter and also check its position in another word.)"
"In this case, rather than looping through letters, you can loop through the index numbers. If you knew the length of the word, you could do this as follows:"

# word = "Book of Mormon"
# number_of_letters = 4

# for index in range(number_of_letters):
#     print(index)
# print()

# Then, you can use the square brackets to access the letter at that index as follows:
# word = "Book"
# numbers_of_letters = 4

# for index in range(numbers_of_letters):
#     letter = word[index]
#     print(f"Index: {index} Letter: {letter}")
# With this example, you have access to both the letter and the index at each step of the loop.


# I. FINDING THE STRING LENGTH
"The previous example assumed the number of letters, or length of the string, would always be 4, but this will not work if the string has more or fewer letters. Instead of typing the 4 directly, you can let the computer find the length by using the 'len function'. The following code shows how to use len to get the length of a string:"
# wife_name = input("What is your wife's name? ")
# letter_count = len(wife_name)

# print(f"Your wife's name has {letter_count} letters.")

"Combining the len function with the earlier loop is very powerful, because now you can iterate through the indexes and letters of strings of any length as follows:"

# word = "Jean Eva Avila"
# number_of_letters = len(word)

# for index in range(number_of_letters):
#     letter = word[index]
#     print(f"Index: {index} Letter: {letter}")
print()

first_name = "Jean and Mike"

# Notice by using enumerate, we specify both i and letter
for i, letter in enumerate(first_name):
    print(f"The letter {letter} is at position {i}.")
print()