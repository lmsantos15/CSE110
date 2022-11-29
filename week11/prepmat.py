# 11 Prepare: Preparation Material

#with open("testing.txt") as preparation_material:
    #for line in preparation_material:
        #print(line)
        #print()

#print("The file is now closed.")  

# OPENING AND READING FROM FILES IN PYTHON
"/*/*/**//*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/"
#my_meals = "lumpia, cake, hotdogs, adobo"

#the_meals = my_meals.split()

#for meal in the_meals:
    #print(meal)

#favorite_meal = the_meals[3]
#print(favorite_meal)

# SPLITTING STRINGS IN PYTHON
"/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/"
#name = "Laur enc e"

#ayawnaman = name.strip()


#print(f"---{ayawnaman}---")

# REMOVING WHITE SPACES FROM STRINGS
"/*/*/*/*/*/*//*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*//*/*/*/*"
with open("testing.txt") as testing_file:
    for line in testing_file:
        line = line.strip()
        parts = line.split(",")
        name = parts[0]
        grade = float(parts[1])

        bonus_grade = grade + 3

        print(f"{name}  - Grade: {grade}, after bonus: {bonus_grade}.")

# READING FILES AND PARSING STRINGS
"*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/**/*/*/"

