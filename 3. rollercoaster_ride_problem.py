# Learning outcome: 'nested-if statement', 'if-elif-else statement', 'multiple if with succession'
# Problem: If user height is above 120cm then they will be allowed rollercoaster riding --> if user age is <12 then them is child & pay $5, elif user age is <18 then them is young & pay $7, else their age is over 18 then them are are adult & pay $12 --> if user wants a phot take then they pay additional $3. 

print("Welcome to the rollercoaster ride!")
height = int(input("What is your height in cm? "))
bill=0

if height >=120:
    print("You can ride rollercoaster ride")
    age = int(input("Enter your age "))

    if(age <=12):
        bill=5
        print("Child tickets are $5")
    elif(age <=18):
        bill=7 
        print("Youth tickets are $7")
    else:
        bill=12
        print("Adults tickets are $12")
        
    wants_photo = input("Do you wants to have a photo take? Type y for Yes and n for No ")
    if wants_photo == 'y':
        bill+=3
        print(f"Your final bill is {bill}")
else:
    print("Sorry, you have to grow taller before you can ride")
