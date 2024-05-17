a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if b == 0:
    print("Error: Division by zero!")
else:
    print(a // b, a / b, sep='\n')
