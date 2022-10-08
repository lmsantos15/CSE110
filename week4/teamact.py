# # 04 Teach: Team Activity

# # THE PROBLEM
# # Determine how fast an object will fall.

# # v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t))


# # m = mass
# # g = gravity
# # t = time
# # c = inner_value
# # p = fluid
# # A = area
# # C = constant

# print()
# # FORMULA v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t))

print("Welcome to the velocity calculator. Please enter the following: \n")

import math

# Mass
mass = float(input("Mass (in kg): "))

# Gravity
gravity = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))

# Time
time = float(input("Time (in seconds): "))

# P = Fluid
fluid = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))

# Area
area = float(input("Cross sectional area (in m^2): "))

# C
constant = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

# c = 1/2 p A C
inner_value = (1/2) * fluid * area * constant
print(f"The inner value of c is: {inner_value:.3f}")

# Velocity
# # v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t))
velocity_time = math.sqrt((mass * gravity) / inner_value) * (1 - math.exp((-math.sqrt(mass * gravity * inner_value) / mass) * time))

# Total calculation
print(f"The velocity after {time} seconds is: {velocity_time:.3f} m/s \n")

import math


print()
print()
print()
print("Velocity of a Bullet")

velocity1 = 2700
distance1 = float(input("What is the distance of the target in meters? "))
# FORMULA Time = distance / velocity
time2 = distance1 / velocity1
print(f"The velocity of the bullet is {time2:.3f}/s.")
print()
# Drop distance calculation
# Formula
# Gravity / 2 * time squared
gravity_pull = 9.8
formula = math.sqrt(gravity_pull / 2 * time2)

print(f"Bullet drop is: {formula:.3f} meters. \n")

# Not really good with math. I hope I made justice with my formula :)