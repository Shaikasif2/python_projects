# def even_odd(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# num = int(input("Enter the number: "))
# print(even_odd(num))


# def is_prime (num):
#     if num >= 1:
#         for i in range (2, int(abs(num) ** 0.5) + 1):
#             if num % i == 0:
#                 return "Not prime number"        
#         return "Prime number"   
# num = int(input("Enter the number: "))
# print(is_prime(num))



# from math import factorial
# def is_strong (num):
#     digits = str(abs(num))  
#     fact_sum = 0
#     for d in digits:
#         fact_sum += factorial(int(d))
#     if fact_sum == abs(num):
#         return f"{num} is a strong number."
#     else:
#         return f"{num} is not a strong number." 
# num = int(input("Enter the number: "))
# print(is_strong(num))    

# def is_armstrong (num):
#     digits = str(abs(num))
#     arm_digits= len(digits)
#     arm_sum = 0
#     for d in digits:
#         arm_sum += int(d) ** arm_digits
#     if arm_sum == abs(num):
#         return f"{num} is armstrong number" 
#     else:
#         return f"{num} is not armstrong number"   
    
# num = int(input("Enter the number: "))
# print(is_armstrong(num))    

# def is_perfect (num):
#     if num <= 1 :
#         return False
#     sum_divisors = 1
#     for i in range (2, int(num** 0.5) + 1):
#         if num % i == 0:
#             sum_divisors += i
#             if i != num // i:
#                 sum_divisors += num // i
#     return sum_divisors == num        
    
# num = int(input("Enter the number: "))
# if is_perfect(num):
#     print(f"{num} is perfect number")
# else:
#      print(f"{num} is not perfect number")      

# def is_sum(num):
#     digits = str(abs(num))
#     sum_digits = sum(int(d) for d in digits)
#     print(sum_digits) 
# num = int(input("Enter the number: "))    
# print(is_sum(num))


# def is_reverse(num):
#     digits = str(abs(num))
#     reversed_num = int(digits[::-1])
#     if num < 0:
#         reversed_num = -reversed_num
#     print(reversed_num)    
# num = int(input("Enter the number: "))
# print(is_reverse(num))    


# def is_palindrone(num):
#     digits = str(num)
#     if str(digits) == str(digits[:: -1]) :
#         print("is palindrone")
#     else:
#         print("Not palindrone")
# num = int(input("Enter the number: "))
# print(is_palindrone(num))


# def is_sum(num):
#     digits = str(int(num))
#     return sum(int(d) for d in digits)
# num = int(input("Enter the number: "))
# print(is_sum(num))


# def is_reverse(num):
#     digits = str(abs(num))
#     reverse_num = int(digits[:: -1])
#     if num < 0 :
#         reverse_num = -reverse_num
#     return reverse_num
# num = int(input("Enter the number: "))
# print(is_reverse(num))    


# def is_palindrone(num):
#     digits = str(abs(num))
#     return str(digits) == str(digits[:: -1])
    
# num = int(input("Enter the number: "))
# if is_palindrone(num):
#     print("Is palindrone")
# else:
#     print("not palindrone") 
# 
# 
from math import factorial
def number_analyzer(num):
    if num > 0 : sign = "Positive Number"
    else: sign = "Negative Number"
    if num % 2 == 0 : parity = " Even Number"
    else: parity = "Odd number"
    digits = str(abs(num))
    sum_digits = sum(int(d) for d in digits)
    reversed_num = int(digits[:: -1])
    if num < 0:
        reversed_num = -reversed_num
    palindrone = str(digits) == str(digits[:: -1])
    fact_sum =  sum(factorial(int(d)) for d in digits)
    strong = fact_sum == abs(num)
    power = len(digits)
    arm_sum = sum(int(d) ** power for d in digits)
    armstrong = arm_sum == abs(num)
    if num > 0:
        sum_divisors =sum(i for i in range (1, num) if num % i == 0)
        perfect = sum_divisors == num
    else:
        perfect = False  
    if num > 1:
        prime = True
        for i in range(2, int(abs(num)** 0.5)+1):
            if i % 2 == 0:
                prime = False
                break
    else:
        prime = False   
             
    return sign, parity, sum_digits, reversed_num, palindrone, strong, armstrong, perfect, prime
num = int(input("Enter the number: "))
s, p, d, r, pal, st, ar, sr, pri = number_analyzer(num)
print("Sign:", s)
print("Parity:", p)
print("Digit Sum:", d)
print("reverse number:", r)
print("palindrone:", pal)
print("Strong number:", st)
print("Armstrong Number:", ar)
print("Perfect Number:",sr)
print("Prime number:", pri)