num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("1.Add  2.Subtract  3.Multiply  4.Divide")
choice = input("choose operation (1/2/3/4):")

if choice == '1':
    print( "result:",  num1 + num2 )
elif choice == '2':
    print("result:", num1 - num2)
elif choice == '3':
    print("result:", num1 * num2)
elif choice == '4':
    print("result:", num1 / num2)
else:
    print("Invalid choice")


