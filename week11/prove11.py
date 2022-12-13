# 11 & 12 Prove: Assignment Milestone

print()

user_year = input("Enter the year of interest: ")
overall_maximum = 0
maximum_expectancy = 0
minimum_expectancy = 1000
overall_minimum = 999
country = ""
years = ""
nation = ""
time = ""
maximum_country = ""
minimum_country = ""
counter = 0
total = 0

print()

with open("life-expectancy1.csv") as file:
    next(file)
    for mike in file:
        mike = mike.split(",")

        entity = mike[0]
        code = mike[1]
        year = mike[2]
        life_expectancy = float(mike[3])

        counter += 1
        total += life_expectancy
        average = total/counter

        if life_expectancy > overall_maximum:
            overall_maximum = life_expectancy
            country = entity
            years = year

        elif life_expectancy < overall_minimum:
            overall_minimum = life_expectancy
            nation = entity
            time = year

        if user_year.lower() == year.lower():

            if life_expectancy > maximum_expectancy:
                maximum_expectancy = life_expectancy
                maximum_country = entity

            elif life_expectancy < minimum_expectancy:
                minimum_expectancy = life_expectancy
                minimum_country = entity

print()
print(f"The overall maximum life expectancy is: {overall_maximum} from {country} in {years}.")
print(f"The overall minimum life expectancy is: {overall_minimum} from {nation} in {time}.")
print()
print(f"The average life expectancy across all countries was {average:2f}.")
print()
print(f"The max life expectancy was in {user_year} is {maximum_expectancy} in {maximum_country}.")
print(f"The minimum life expectancy was in {user_year} is {minimum_expectancy} in {minimum_country}")    
print()



