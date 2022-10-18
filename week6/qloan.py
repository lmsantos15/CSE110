# 06 Prepare: Checkpoint


print()
print("For each of these questions, please and it with 1 - 10, 10 being the highest: ")
print()
loan = float(input("How large is the loan? "))
credit = float(input("How good is your credit history? "))
income = float(input("How high is your income? "))
down = float(input("How large is your down payment? "))
pautang = False

if loan >= 5:
    if credit >= 7 and income >=7:
        pautang = True
    elif credit >= 7 or income >= 7:
        if down >= 5:
            pautang = True
        else:
            pautang = False
    else:
        pautang = False

else:
    if credit < 4:
        pautang = False
    else:
        if income >= 7 or down >= 7:
            pautang = True
        elif income >= 4 and down >= 4:
            pautang = True
        else:
            pautang = False

if pautang:
    print("You request has been granted!")
else:
    print("Request if declined.")
print()

