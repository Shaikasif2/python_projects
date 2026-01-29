import random
secret_number = random.randint(1, 1000)
guess = int(input("Guess the number between 1 to 1000: "))
if guess == secret_number:
    print("Congratulations! You guessed the correct number.")
elif guess < secret_number:
    print("Your guess is too low.")    
elif guess > secret_number:    
    print("Your guess is too high.")
else:
    print(f"Sorry, the correct number was {secret_number}. Better luck next time!")

print("The secret number was:", secret_number)    