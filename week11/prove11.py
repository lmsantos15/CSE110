# 11 Prove: Assignment Milestone

print()

with open("life-expectancy1.csv") as the_life_expectancy:

    i = 0

    "The lowest life expentancy"

    lowest_life_expectancy = 1000
    lowest_country = ""
    lowest_year = 0

    "The highest life expectancy"

    highest_life_expectancy = 0
    highest_country = ""
    highest_year = 0


    highest_life_expectancy = 0
    for buhay in the_life_expectancy:
        i += 1

        

        life_strip = buhay.strip()

        life_split = life_strip.split(",")

        country = life_split[0] # Country

        code = life_split[1] # Code

        year = life_split[2] # Year

        life_exp = life_split[3] # String for Life Expectancy


        if i > 1:
            life_exp = float(life_exp)

            if life_exp < lowest_life_expectancy:
                lowest_life_expectancy = life_exp
                lowest_country = country
                lowest_year = year


            if life_exp > highest_life_expectancy:
                highest_life_expectancy = life_exp
                highest_country = country
                highest_year = year

print()
print(f"{lowest_country} - {lowest_year} - {lowest_life_expectancy}")
print(f"{highest_country} - {highest_year} - {highest_life_expectancy}")               
print()








