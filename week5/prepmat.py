# # Symbol                    Operation
# # >                         Greater than
# # <                         Less than
# # >=                        Greater than or equal to
# # <=                        Less than or equal to
# # ==                        is equal to
# # !=                        is not equal to
# print()
# price = input("How much is the product? ")
# price = float(price)


# if price >= 1.00:
#     tax = .09
#     print("The tax rate is: " + str(tax))

# else:
#     tax = 0
#     print("The tax rate is: " + str(tax))
# print()
# print()


print()
country = input("Enter your home country: ")
if country.lower() == "canada":
    print("You must like hotdogs!")
else:
    print("You are not from Canada")
print()
# USING if AND elif
province = input("What is your home province? ")
if province.lower() == "Alberta":
    tax = 0.05
elif province.lower() == "Nunavut":
    tax = 0.05
elif province.lower() == "Ontario":
    tax = 0.13
else:
    tax = 0.15
    print("Your tax rate is: " + str(tax))
print()
