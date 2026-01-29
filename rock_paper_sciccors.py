import random
choice = input("Enter your choice (rock, paper, scissors): ").lower()
computer_choice = random.choice(['rock', 'paper', 'scissors'])
print(f"Computer chose: {computer_choice}")
if choice == computer_choice:
    print("It's a tie!")
elif (choice == 'rock' and computer_choice == 'scissors') or \
     (choice == 'paper' and computer_choice == 'rock') or \
     (choice == 'scissors' and computer_choice == 'paper'):    
    print("You win!")
else:
    print("You lose!")    