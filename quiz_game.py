score = 0
q1 = input("What is the capital of Telangana? ").lower()
if q1 == "Hyderabad".lower():
    score += 1
q2 = input("What is 8*5?")
if q2 == "40":    
    score += 1
q3 = input("Who is the CEO of Tesla? ").lower()
if q3 == "Elon musk".lower():
    score += 1

print(f"Your total score is: {score}/3")    