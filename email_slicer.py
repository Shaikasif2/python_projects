email = input("Enter your email address: ")
username  = email.split("@")[0]
domain = email.split("@")[1].split(".")[0]
print(f"Username: {username}")
print(f"Domain: {domain}")