'''Problem: Program should automatically calculates bill for the user based on no. of options.

Given info.:
Small pizza (S): $15
Medium pizza (M): $20
Large pizza (L): $25
Add pepperoni for small pizza (Y or N): +$2
Add pepperoni for medium or large pizza (Y or N): +$3
Add extra cheese for any size pizza (Y or N): +$1 '''

'''Expected output:
Welcome to Python Pizza Deliveries!
What size pizza do you want? S, M or L: L
Do you want pepperoni on your pizza? Y or N: Y
Do you want extra cheese? Y or N: N
Your final bill is: $28   '''


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

#todo: work out how much they need to pay based ontheir size choice
bill = 0
if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25
else:
    print("You entered wrong input size")

#todo: work out how much to add on their bill based on their pepperoni choice
if pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3

#todo: work out their final amount based on whether if they want extra cheese
if extra_cheese == 'Y':
    bill += 1
print(f"Your final bill is ${bill}")
