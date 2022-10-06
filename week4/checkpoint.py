# Unit Conversion

import math
# Purpose: Convert degrees in Fahrenheit to Celsius.
degrees_f = float(input("What is the temperature in Fahrenheit? "))
degrees_c = (degrees_f - 32) * 5 / 9

print(f"The temperature is celcius is {degrees_c:.1f} degrees.")
print()
