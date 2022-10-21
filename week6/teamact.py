# 06 Teach: Team Activity
# Amusement Park Rides

print()


age1 = int(input("What is the age of the first rider? "))
height1 = int(input("What is the height of the first rider? "))
second_rider_present = input("Is there a second rider (Yes/No)? ")
print()

if age1 >= 18 and height1 >= 62 and second_rider_present.lower() == "no":
    print("Welcome to the ride. Please be safe and have fun!")

elif age1 >= 18 and height1 >= 62 and second_rider_present.lower() == "yes":
    age2 = int(input("What is the age of the second rider? ")) 
    height2 = int(input("What is the height of the second rider? "))
    print()
    
    if age2 >= 18 or height2 <= 35:
        print("Sorry, you may not ride.\n")

    elif age2 >= 18 or height2 >= 36:
        print("Welcome to the ride. Please be safe and have fun! \n")

elif age1 <= 17 and height1 <= 61 and second_rider_present.lower() == "no":
    print("Sorry, you may not ride. \n")




