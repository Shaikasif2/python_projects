weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height * height)
print(f"Your BMI is:", round(bmi, 2))
if bmi < 18.5:
    print("You are underweight.")
elif bmi < 24.9:
    print("You have a normal weight.")
elif bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")

