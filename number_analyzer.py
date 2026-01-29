num = int(input("Enter a number: "))
# Determine if the number is positive, negative, or zero and if it is even or odd
if num == 0:
    print("The number is zero and even.")
else:
    if num > 0:
        sign = "positive"
    else:
        sign = "negative"    
    if num % 2 == 0:
        parity = "even"
    else:
        parity = "odd"    
    print(f"The number is {sign} and {parity}.")  

# Check if the number is prime
if num > 1:
    for i in range(2, int(abs(num) ** 0.5) + 1):
        if (num % i ) == 0:
            print(f"{num} is not a prime number.")
            break
        else:
            print(f"{num} is a prime number.")
            break
else:
    print(f"{num} is not a prime number.")     

# Calculate the sum of the digits        
digits = str(abs(num))  
digits_sum = sum(int(d) for d in digits)
print("The sum of the digits is:", digits_sum)       

# Reverse the digits and check for palindrome
reversed_num = int(digits[::-1])
if num < 0:
    reversed_num = -reversed_num
print("The reversed number is:", reversed_num)

# Check if the number is a palindrome
if str(digits) == str(digits)[::-1]:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")

# Check if the number is perfect
if num > 0:
    sum_divisors = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_divisors += i
    if sum_divisors == num:
        print(f"{num} is a perfect number.")
    else:
        print(f"{num} is not a perfect number.")     
else:
    print(f"{num} is not a perfect number.")    

# Check if the number is an Armstrong number
arm_digits = len(digits)
arm_sum =  0
for d in digits:
    arm_sum += int(d) ** arm_digits
if arm_sum == abs(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")    

# Check if the number is a strong number
from math import factorial
fact_sum = 0
for d in digits:
    fact_sum += factorial(int(d))
if fact_sum == abs(num):
    print(f"{num} is a strong number.")
else:
    print(f"{num} is not a strong number.")    