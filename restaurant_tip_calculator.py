print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))    #Ex: 200
tip = int(input("How much tip would you like to give in percentage? Don't add percentage. Example input: 10, 12 0r 15? "))   #Ex: 10
people = int(input("How many people to split the bill?"))    #Ex: 8

# formula: bill + (bill * tip / 100)
tip_in_percentage = tip /100        # 10/100 = 0.10
total_tip = bill * tip_in_percentage    # 200 * 0.10 = 20
total_bill = bill + total_tip   # 200 + 20 = 220
split_into_people = total_bill / people     # 220 / 8 = 27.50000000
total_amount = round(split_into_people, 2)

print(f"Each person would have to pay bill ${total_amount}")
