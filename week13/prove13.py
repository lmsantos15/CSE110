# 13 Prove: Assignment
"Wind Chill Calculations"

print()

# Formula

# For Celcius - (F - 32) x 5/9
# For Fahrenheit - (C x 9/5) + 32

"Wind chill"
def wind_chill(air_temp, wind_speed):
    return 35.74 + (0.6215 * air_temp) - (35.75 * wind_speed**0.16) + (0.4275 * air_temp * wind_speed * wind_speed**0.16)

print()

# Getting the Fahrenheit
def fahrenheit(temp):

    return temp

# Getting the Celcius
def celcius(temp):

    return temp * (9 / 5) + 32


# Computing the Temperature
def temperature_computation(temp_type, value1):

    temperature = -1

    if temp_type.upper() == "F":

        temperature = fahrenheit(value1)

    elif temp_type.upper() == "C":

        temperature = celcius(value1)

    return temperature


# Whole process
temperature_type = ""

while temperature_type != "Quit":
    print()
    temp_num = float(input("What is the temperature? "))
    print()
    temp_type = input("Fahrenheit or Celcius (F/C)? ")
    print()

    temp_type = temp_type.upper()

    if temp_type == "F":

        temperature = temperature_computation(temp_type, temp_num)

        wind_speed = 0

        air_temp = 0

        for hangin in range(12):

            wind_speed = wind_speed + 5


            print()
            print(f"At temperature {temperature} F, and the wind speed {wind_speed} mph, the windchill is: {wind_chill(temp_num, wind_speed):.2f} F")

    elif temp_type == "C":

        temperature = temperature_computation(temp_type, temp_num)

        wind_speed = 0

        air_temp = 0

        for hangin in range(12):

            wind_speed = wind_speed + 5
            
            air_temp = air_temp - 0.001

            print()
            print(f"At temperature {temperature} F, and the wind speed {wind_speed} mph, the windchill is: {wind_chill(air_temp, wind_speed):.2f} F")

# Getting the wind chill formula
# Wind Chill (ºF) = 35.74 + 0.6215T - 35.75(V0.16) + 0.4275T(V0.16)
# Where,T= Air Temperature (ºF) V= Wind Speed (mph)





