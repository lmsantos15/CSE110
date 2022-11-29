# 12 Prepare: Preparation Material

"FINDING THE MAX OR MINIMUM"
# numbers = [11, 22, 33, 44, 55, 66, 77, 88, 99]

# largest_number = numbers[0]

# for number in numbers:
#     if number < largest_number:

#         largest_number = number

# print(f"The largest is: {largest_number}")


"KEEPING TRACK OF THE ITEM THAT IS THE MAX OR MIN"
shopping_cart = [["chips", 2.99], ["bread", 2.50], ["milk", 5.77]]

# max_price = -1

# for item in shopping_cart:
#     price = item[1] # The price is the second part of the item

#     if price > max_price:
#         # This is the new max
#         max_price = price

# print(f"The maximum price is: {max_price}")
"If we want to find the name of the item that is the most expensive, we need to declare a variable (for example, max_product) before the loop to keep track of the product that had the maximum price."

max_price = -1
max_product = "" # It doesn't matter what you set this to, it just needs to be declared

for item in shopping_cart:
    product_name = item[0] # Product name is the first part
    price = item[1] 

    if price > max_price:
        # This is the new max
        max_price = price

        # Also save this product name as the max product
        max_product = product_name

print(f"The maximum price is: {max_price}")
print(f"The product with the maximum price is: {max_product}")

"OTHER CODE WITH LOOPS AND FILES"
# In addition to the code samples you've seen here, keep in mind that you can use all of the other components you have learned throughout the semester in conjunction with files.

