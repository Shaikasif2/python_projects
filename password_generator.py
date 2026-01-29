import random
import string
password_length = int(input("Enter the desired password length: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ""
for i in range (password_length):
    password += (random.choice(characters)) 
print(f"Generated password: {password}")