print("1.calculator  2.random number guesser  3.even odd checker 4.age calculator 5.temperature converter 6.bmi calculator 7.multiplication table 8.random number generator 9.countdown timer")
menu_choice=int(input("Enter your choice: "))
if menu_choice == 1:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("1.Addition 2.Subtrsction 3.Multiplication 4.Division")
    cal_choice = int(input("Enter your choice: 1/2/3/4:"))
    if cal_choice == 1 :
        print(f"The sum is: {num1 + num2}")
    elif cal_choice == 2 :    
        print(f"The difference is: {num1 - num2}")
    elif cal_choice == 3 :    
        print(f"The product is: {num1 * num2}")
    elif cal_choice == 4 :    
        print(f"The quotient is: {num1 / num2}")
    else:
        print("Invalid input")    

elif menu_choice == 2:
    import random
    secret_number = random.randint(1, 100)
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
    else:
        print(f"Sorry, the correct number was {secret_number}.")            

elif menu_choice == 3:
    num = int(input("Enter a number: "))
    if  num % 2 == 0:
        print(f"{num} is an even number.")        
    else:
        print(f"{num} is an odd number.")    

elif menu_choice == 4:        
    current_year = int(input("Enter the current year: "))
    birth_year = int(input("Enter your birth year: "))
    age = current_year - birth_year
    print(f"You are {age} years old.")

elif menu_choice == 5:    
    celsius = float(input("Enter temperature in Celsius: "))
    farenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {farenheit}°F")

    farenheit = float(input("Enter temperature in Farenheit: "))
    celsius = (farenheit - 32) * 5/9
    print(f"{farenheit}°F is equal to {celsius}°C")

elif menu_choice == 6:
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    bmi = weight / (height ** 2)
    print(f"Your BMI is: {round(bmi, 2)}")
    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        print("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        print("You are overweight.")   
    else:     
        print("You are obese.")     

elif menu_choice == 7:        
    num = int(input("Enter a number to display its multiplication table: "))
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

elif menu_choice == 8:
    import random        
    start = int(input("Enter the start number: "))
    end = int(input("Enter the end number: "))
    random_number = random.randint(start, end)
    print(f"Random number between {start} and {end}: {random_number}")

elif menu_choice == 9:    
    import time 
    seconds = int(input("Enter the number of seconds for countdown: "))
    while seconds:
        print(seconds)
        time.sleep(1)
        seconds -= 1
    print("Countdown finished!")    

else:
    print("Invalid choice. Please select a valid option from the menu.")