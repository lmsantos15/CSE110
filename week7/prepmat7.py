# 07 Prepare: Preparation Material
print()

# LOOP | while
asset = float(input("How much is your asset? "))

while asset < 0:
    print("Asset must be positive.")
    asset = float(input("How much is your asset? "))
    

print(f"That is a huge amount {asset:.2f}!")
print()


# Computer counting
count = 1

while count <= 10:
    print(f"The number is {count}.")
    count = count +1

print("Wonderful!")


