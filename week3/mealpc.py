import numbers


# 03 Prove: Milestone - Meal Price Calculator
print()
# The Meal Calculator

drinks_num = int(input("How many Sodas? "))
drinks_price = float(input("Sodas' price: "))

# Number of children meal and adult meal
child_meal = float(input("What is the child's meal price? "))
adult_meal = float(input("What is the adult's meal price? "))

# Total number of children and adult
children_num = int(input("How many children are there? "))
adult_num = int(input("How many adults are there? "))

# Cakes Milestone
cake_num = float(input("How many cakes? "))
cake_price = float(input("Cake's price: "))

# Tax Rate
tax_rate = float(input("What is the sales tax rate? "))

# Multiply the children's meal and children's number
child_total_amount = child_meal * children_num

# Multiply the children's meal and adult's number
adult_total_amount = adult_meal * adult_num

# Drinks' total
drinks_total = drinks_num * drinks_price

# Cakes' total
total_cake = cake_num * cake_price

# Children and Adult total amount
subtotal = child_total_amount + adult_total_amount + drinks_total + total_cake

# Sales Tax
sales_tax = subtotal * tax_rate / 100

# Total Amount
total = subtotal + sales_tax
print()
print()
# Subtotal
print(f"Subtotal: ${subtotal}")

# Total Sales Tax
print(f"Sales Tax: ${round(sales_tax, 2)}")

# Total Amount
print(f"Total: $ {round(total, 2)}")

# Total payment amount
amount = float(input("What is the payment amount? "))

# Total Change
change = amount - total
print()
# Display Change
print(f"Change: ${round(change, 2)}")


