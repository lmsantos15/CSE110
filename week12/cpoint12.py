# 12 Prepare: Checkpoint

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

print()

# Start our people_and_age variable at something larger than anyone we'll find
people_and_age = 9999

# This will keep track of the person with the youngest age
people_name = ""

"This will go through each person in the list"
for person_list in people:

    parts = person_list.split() # By default this will split on the space

      # Set variables for the two different parts
    name = parts[0]
    age = int(parts[1])


     # Check to see if this current person is younger than the youngest
     # that we have seen so far
    if age < people_and_age:
        # This person is the new "youngest"
    
        people_and_age = age # Save their age as the new youngest

        people_name = name # Save their name as the youngest name

print()
# Outside of the loop, so we are all done now
print(f"The youngest person is: {people_name} with the age of {people_and_age}.")
print()






