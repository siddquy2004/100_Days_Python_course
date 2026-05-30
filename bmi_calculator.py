# bmi = body mass index
# bmi calculator is a tool used to measure body mass/weight is healthier w.r.t. height or not.
# bmi calculator takes 2 inputs height & weight. Then it outputs weight of a person is underweight, normal(healthy), overweight, obese
''' bmi standard formula, bmi= weight(kg) / height^2 (m^2)
    if user wants to give inputs weight in pound (lb) and height in inches (in) then bmi formula is modified
    bmi= 703 * weight(lb) / height^2 (in^2) '''
''' Underweight: BMI < 18.5
    Normal weight: 18.5–24.9
    Overweight: 25–29.9
    Obese: BMI ≥ 30 '''
    
# BMI Calculator

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

print("Your BMI is:", round(bmi, 2))

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")
    
