# Use functions instead of repeating code
from datetime import datetime



# def print_time():
#     print("Task Completed")
#     print(datetime.datetime.now())
#     print()

# first_name = "Mike"
# print_time()

# for x in range(0,10):
#     print(x)
# print_time()

# What if I want a different message displayed?

"Print the current time and task name"
# def print_time(task_name):
#     print(task_name)
#     print(datetime.now())
#     print()

# first_name = "Jean"
# print_time("First name assigned")

# for x in range(0,10):
#     print(x)
# print_time("Loop Completed")



# Here's another example where the code looks different but we are doing the same logic over and over

# first_name = input("Enter your first name: ")
# first_name_initial = first_name[0:1]
# last_name = input("Enter your last name: ")
# last_name_initial = last_name[0:1]

# print("Your initials are: " + first_name_initial + last_name_initial)

"I can still use a function, but this time my function returns a value"
def get_initial(name):
    initial = name[0:1]
    return initial

first_name = input("Enter your first name: ")
first_name_initial = get_initial(first_name)

last_name = input("Enter your last name: ")
last_name_initial = get_initial(last_name)

print("Your initials are: " + first_name_initial + last_name_initial)