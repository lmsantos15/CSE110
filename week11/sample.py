i = 0

with open("life-expectancy1.csv") as life_expectancies:
    year_of_interest = int(input('please enter a year: '))
    #lowest
    lowest_exp = 1000
    lowest_country = ''
    lowest_yr = 0
    high_exp =0
    high_country = ''
    high_yr = 0

    total = 0
    counter = 0
    max_exp = 0
    max_country = ''
    min_exp = 1000
    min_country = ''
    
   
    for it in life_expectancies:
            i += 1
            clean_str = it.strip() # remove spaces
            clean_spl = clean_str.split(',') 
            country = clean_spl[0]# Country 
            code = clean_spl[1] # code
            year = clean_spl[2] # year
            life_exp = clean_spl[3] #life expectancies

            if i > 1:
                life_exp = float(life_exp)


         # find the lowest expentancy 
            
                if life_exp < lowest_year:

                    lowest_exp = life_exp
                    lowest_country = country
                    lowest_year = year

                if life_exp >  high_exp:

                    high_exp =life_exp
                    high_country = country
                    high_yr = year

                if year_of_interest == year:

                    total += life_exp
                    counter += 1
                    average = total/counter
                    

                    if life_exp > max_exp:
                        max_exp = life_exp
                        max_country = country

                    if life_exp < min_exp:
                    
                        min_exp = life_exp
                        min_country = country
                        
print(f'The over all max expectancy is :{high_exp} from {high_country} in {high_yr}')
print(f'The over all min expectancy is :{lowest_exp} from  {lowest_country} in {lowest_yr}')

print(f'For the year of {year_of_interest}:')
# print(f'The average life expectancy across all the countries was {average}')
print(f'The max life expectancy was in {max_country} with {max_exp:.2f}')
print(f'the minimum life expectancy was in {min_country} with {min_exp:.2f}')