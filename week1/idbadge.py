# I had to use the basic of the basic in Python
# since this is my first writing this kind of program

print()
print("Please enter the following information:")

first_name = input("Enter your first name: ")

last_name = input("Enter your last name: ")

email_address = input("What is your email address: ")

phone_number = input("What is your phone number? ")

job_title = input("What is your job title? ")

id_number = input("What is your ID number? ")

hair_color = input("Color of your hair: ")

month = input("Starting month: ")

eye_color = input("Eye color: ")

training = input("Completed advance training? ")

print()
print()
print()
print("The ID Card is: ")
print("----------------------------------------")
print()
print(f"{last_name.upper()}, {first_name.upper()}")
print("Job Title: " + job_title.title())
print("ID: " + id_number)
print()
print(email_address.lower())
print(phone_number)
print()
# Had to copy the code from teach02_stretch_sample.py since I have no clear knowledge
# on how I can make the proper spacing despite watching several videos.
print(f"Hair: {hair_color.capitalize():15} Eyes: {eye_color.capitalize()}")
print(f"Month: {month.capitalize():14} Training: {training.capitalize()}")
print("----------------------------------------")



