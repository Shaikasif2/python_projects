# balance = 5000
# pin = 1207

# entered_pin = int(input("Enter the pin:"))
# if entered_pin == pin:
#     while True:
#         print("-------- ATM MENU --------")
#         print("1.Check balance")
#         print("2.Deposit Money")
#         print("3.Withdraw Money")
#         print("4.Exit")
#         choice = int(input("Enter your choice: "))

#         if choice == 1:
#             print("The available balance is:",balance)
#         elif choice == 2:
#             amount = float(input("Enter the deposit amount:"))
#             if amount> 0:
#                 balance += amount
#                 print("Deposited sucessfully")
#             else:
#                 print("Invalid amount")
#         elif choice == 3:
#             amount = float(input("Enter the amount:"))
#             if amount > 0:
#                 balance -= amount
#                 print("Please collect your cash")
#             else:
#                 print("Invalid amount")
#         elif choice == 4:
#             print("Thank you for using ATM.")
#             break                         
#         else:
#             print("Invalid option")

# else:
#     print("Wrong pin")


# def atm_simulator():
#     balance = 5000
#     pin = 1207
#     attemp = 3
#     while attemp > 0:
#         try:
#             entered_pin= int(input("Eneter the pin:"))
#         except ValueError:
#             print("Please enter the Numeric digits only.")
#             continue    
#         if entered_pin == pin :
#             print("Login sucessful. Welcome to the ATM.")
#             while True:
#                 print("------ ATM MENU ------")
#                 print("1.balance")
#                 print("2.deposit money")
#                 print("3.withdraw money")
#                 print("4.Change pin")
#                 print("5.Exit")
#                 try:
#                     choice = int(input("Enter the choice:"))
#                 except ValueError:
#                     print("Invalid input, Please enter the valid number (1-4)")
#                     continue    
#                 if choice == 1:
#                     print("The availabe balance is:",balance)
#                 elif choice == 2:
#                     amount = float(input("Enter the amount:"))
#                     if amount > 0 :
#                         balance += amount
#                         print("Deposit sucessfully, New Balance: ", balance) 
#                     else:
#                         print("Invalid option")
#                 elif choice == 3:
#                     amount = float(input("Enter the amount:" ))
#                     if 0 < amount <= balance:
#                         balance -= amount
#                         print("Please collect your cash")
#                         print("Available balance:", balance)
#                     elif amount > balance:
#                         print("Insufficcient Funds")    
#                     else:
#                         print("Invalid option")
#                 elif choice == 4:
#                     current_pin = int(input("Enter the pin for thr verification:"))
#                     if current_pin == pin:
#                         new_pin = int(input("Enter the new pin:"))
#                         confirm_pin = int(input("Re-enter to confirm the pin:"))
#                         if new_pin != confirm_pin:
#                             print("The new pin and re-entered pin is not matched. Pin generation failed")
#                         else:
#                             pin = new_pin
#                             print("The new pin is genereted sucessfully and updated")   
#                     else:
#                         print("Incorrect pin entered. Try again. ")    
                   

#                 elif choice == 5:
#                     print("Thank you for using the ATM.")
#                     return
#                 else:
#                     print("Inavalid option. Please try again.")
                    
#         else:
#             attemp -= 1
#             if attemp > 0:
#                 print(f"Incorrect pin, you have {attemp} more guesses.")
#             else:
#                 print("Too many failed attemps, you account has been locked.")            
        

# atm_simulator()


# def atm_simulator():
#     balance = 50000
#     pin = 1207
    
#     attemp = 3
#     while attemp > 0:
#         try:
#             entered_pin = int(input("Enter the pin:"))
#         except ValueError:
#             print("Enter the pin in numeric digits")
#             continue    
#         if entered_pin == pin:
#             print("You are Login. Wlecomre to the ATM.")
#             while True:
#                 print("------- ATM MENU --------")
#                 print("1.Balance")
#                 print("2.Deposit Money")
#                 print("3.Withdraw Money")
#                 print("4.Change pin")
#                 print("5.Exit")
#                 try:
#                     choice = int(input("Enter the choice:"))
#                 except ValueError:
#                     print("Enter the choice in digits from (1-5)")
#                 if choice == 1:
#                     print("THe Available balance:", balance)
#                 elif choice == 2:
#                     amount = float(input("Enter the amount:"))
#                     if amount > 0:
#                         balance += amount
#                         print("Deposited sucessfully. New balance:", balance)
#                     else:
#                         print("Invalid amount")
#                 elif choice == 3:
#                     amount = float(input("Enter the amount:"))
#                     if amount < 0 <= balance:
#                         balance -= amount
#                         print("Please collect your cash. Remaining balance:", balance)   
#                     elif amount > balance:
#                         print("Insufficient funds")
#                     else:
#                         print("Invalid amount")
#                 elif choice == 4:
#                     verification_pin = int(input("Enter the pin for the verification:"))
#                     if verification_pin == pin:
#                         new_pin = int(input("Enter the new pin:"))
#                         confirm_pin = int(input("re-enter the pin for the confirmation:"))
#                         if new_pin == confirm_pin:
#                             pin = confirm_pin
#                             print("The pin is generated sucessfylly.")                   
#                         else:
#                             print("The new pin and re-entered pin does not matched. The pin generation failed.")
#                     else:
#                         print("Incorrect pin. Enter the correct pin to change pin.")
#                 elif choice == 5:
#                     print("Thank you for using ATM.Visit again")  
#                     return  
#                 else:
#                     print("Invalid option. Make sure to enter the coorect option.")        
#         else:
#             attemp -= 1
#             if attemp > 0:
#                 print(f"Incorrect pin. you have {attemp} more guesses.")
#             else:
#                 print("You have tried too many failed attemps. The account has been locked.") 


# atm_simulator()
            
                        
def check_balance(balance):
    print("The Available balance is:",balance)

from datetime import datetime
def deposit_money(balance , transctions):
    amount = float(input("Enter the amount:"))
    if amount > 0 :
        balance += amount
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transctions.append({
            "type":"Deposit",
            "amount":amount,
             "time": now
       })
        print("Deposited sucessfully. New balance:",balance)
    else:
        print("Invalid amount.")
    return balance    

def withdraw_money(balance, transctions):
    amount = float(input("Enter the amount:"))
    if 0 < amount <= balance:
        balance -= amount
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transctions.append({
            "type":"Withdraw",
            "amount":amount,
            "time": now
        })
        print("Please collect your cash. Remaing balance:", balance)        
    elif amount > balance:
        print("Insuffficient Funds.")
    else:
        print("Invalid amount.")
    return balance    

def change_pin(pin):
    verification_pin = int(input ("Enter the pin for the verification:"))
    if verification_pin == pin:
        new_pin = int(input("Enter the new pin:"))
        confirm_pin = int(input("re-enter the pin to confirm it:"))
        if new_pin == confirm_pin:
            print("The new pin is generated sucessfully.")
            return new_pin
        else:
            print("The charactes of new and re-enter pin does not match. Try again")  
    else:
        print("Incorrect pin. Enter the correct pin to generate new pin.")
    return pin    


def atm_exit():
    print("Thank you for using ATM. Visit again.")      


def view_transaction_history(transactions):
    if not transactions:
        print("No transactions yet.")
        return
    print("----\n Transactions hostory -----")
    for i , t in enumerate(transactions,1):
        print(f"{i}.{t['type']} | {t['amount']} | {t['time']}")
    

def show_menu():
    print("------- ATM MENU --------")
    print("1.ckeck balance")
    print("2.Deposit money")
    print("3.Withdraw money")
    print("4.Change pin")
    print("5.View Transaction history")
    print("6.Save Transactions and Exit")
    return int(input("Enter the choice:"))

def save_transactions (transactions):
    path = r"C:\Users\asifs\OneDrive\Desktop\transaction.txt"
    with open(path , "a") as file:
        for t in transactions:
            line = f"{t['type']} | {t['amount']} | {t['time']}\n"
            file.write(line)
    print("Transaction saved sucessfully.")        
            

def atm():
    balance = 50000
    pin = 1207
    transactions = []
    attemp = 3
    while attemp > 0:
        try:
            entered_pin = int(input("Enter the pin:"))
        except ValueError:
            print("Enter the numberical digits.")
            continue
        if entered_pin == pin :
            print("YOu have Login. Welcome to the ATM.")
            while True:
                choice = show_menu()
                if choice == 1:
                    check_balance(balance)
                elif choice == 2:
                    balance = deposit_money(balance,transactions)
                elif choice == 3:
                    balance = withdraw_money(balance,transactions)
                elif choice == 4:
                    pin = change_pin(pin)
                elif choice == 5:
                    view_transaction_history(transactions)    
                elif choice == 6:
                    save_transactions(transactions)
                    atm_exit()
                    return
                else:
                    print("Invalid option.")                  
        else:
            attemp -= 1
            if attemp > 0:
                print(f"Incorrect pin. You have {attemp} more guesses.")
            else:
                print("You have attemp too many failed attemps. Your account has locked.")

atm()



