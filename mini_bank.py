from datetime import datetime
import csv
import os
def create_account():
    acc_no = int(input("Create the account number:"))
    name = input("Enter your name:")
    pwd = input("Create a strong password:")
    pin = int(input("Create the pin:"))
    balance = 500000
    path = r"E:\account.csv"
    heading = ["acc_no", "name", "pwd", "pin", "balance"]
    file_exists = os.path.isfile(path)
    with open(path, "a+", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(heading)
        writer.writerow([acc_no, name, pwd, pin, balance])
    print("Your Account have created sucessfully.")

def login():
    acc_no = int(input("Enter the account number:"))
    pwd = input("Enter the password:")
    path = r"E:\account.csv"
    with open (path, "r") as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            if int(row[0]) == acc_no and row[2] == pwd:
                return int(row[0]), int(row[3]), float(row[4])
    return None

def save_transactions(acc_no, ttype, amount, balance):
    path = r"E:\transaction.csv"
    heading = ["acc_no", "ttype", "amount", "time", "balance"]
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = os.path.isfile(path)
    with open(path, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(heading)
        writer.writerow([acc_no, ttype, amount, now, balance])
    print("Transactions saved sucessfully.")

def view_trasactions(acc_no):
    path = r"E:\transaction.csv"
    with open(path , "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if int(row[0]) == acc_no:
                print(row) 

def change_pin(acc_no):
    path = r"E:\account.csv"
    new_pin = int(input("Enter the new pin:"))
    confirm_pin = int(input("Confirm the pin:"))
    rows = []
    if new_pin == confirm_pin:
        with open(path, "r") as file:
            reader = csv.reader(file)
            rows = list(reader)

        with open(path, "w" , newline="") as file:
            Writer = csv.writer(file) 
            for row in rows:
                if row[0] == "acc_no":
                    Writer.writerow(row)
                elif int(row[0]) == acc_no:
                    row[3] = confirm_pin
                    Writer.writerow(row)
                else:
                    Writer.writerow(row)
        print("Pin has updated sucessfully.")
    else:
        print("The characters of new pin and confirm pin is not matched.")

def change_pwd(acc_no):
    path = r"E:\account.csv"
    new_password = input("Enter the new password:")
    confirm_password = input("Confirm the password:")
    rows = []
    if new_password == confirm_password:
        with open(path, "r") as file:
            reader = csv.reader(file)
            rows = list(reader)
        with open (path, "w" , newline="") as file:
            writer = csv.writer(file)
            for row in rows:
                if row[0] == "acc_no":
                    writer.writerow(row)
                elif int(row[0]) == acc_no:
                    row[2] = confirm_password
                    writer.writerow(row)
                else:
                    writer.writerow(row)         
        print("The password is updated sucessfully.")            
    else:
        print("The chracters are mismatched.")

def update_balance(acc_no,balance):
    path = r"E:\account.csv"
    with open(path, "r") as file:
        rows =list(csv.reader(file))
    with open(path, "w", newline="") as file:
        Writer = csv.writer(file)
        for row in rows:
            if row[0] == "acc_no":
                Writer.writerow(row)
            elif int(row[0]) == acc_no:
                row[4] = str(balance)
                Writer.writerow(row)
            else:
                Writer.writerow(row)               

def atm(acc_no, pin, balance):
    transactions = []
    while True:
        print("---- ATM MENU-----")
        print("1.check balance")
        print("2.Deposit Money")
        print("3.Withdraw Money")
        print("4.view transactions")
        print("5.Change pin")
        print("6.Change password")
        print("7.Logout")
        ch = int(input("Enter the choice:"))
        if ch == 1:
            print("The available balance:", balance)
        elif ch == 2:
            amount = float(input("Enter the amount:"))
            if amount > 0 :
                balance += amount
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                transactions.append({
                    "ttype":"Deposit",
                    "amount": amount,
                    "time": now,
                    "balance": balance
               })
                save_transactions(acc_no, "Deposit", amount, balance)
                update_balance(acc_no, balance)
                print("Deposit sucessfully. New balance:", balance)
            else:
                print("Invalid amount.")       
        elif ch == 3:
            amount = float(input("Enter the amount:"))
            if 0 < amount <= balance:
                balance -= amount
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                transactions.append({
                    "ttype":"Withdraw",
                    "amount": amount,
                    "time": now,
                    "balance": balance
               })
                save_transactions(acc_no, "Withdraw", amount, balance)
                update_balance(acc_no, balance)
                print("Withdraw sucessfully. Remaing balance:", balance)
            elif amount > balance:
                print("Insufficient funds.")
            else:
                print("Invalid amount.")
        elif ch == 4:
            view_trasactions(acc_no)
        elif ch == 5:
            change_pin(acc_no)
        elif ch == 6:
            change_pwd(acc_no)
        elif ch == 7:
            print("Logout from the account.")
            break
        else:
            print("Invalid choice.")


print("1.Create Account")
print("2.Login")
choice = int(input("Enter the choice:"))
if choice == 1:
    create_account()    
elif choice == 2:
    user = login()
    if user :
        acc_no, pin, balance = user
        print("Login sucessful.Welcome to your Account.",)
        atm(acc_no, pin, balance)
    else:
        print("Invalid Login.")    
else:
    print("Invalid choice.")  
           