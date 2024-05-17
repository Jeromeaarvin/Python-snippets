opt = input("Choose operation (+, -, *, /): ")
a = int(input("Enter num 1: "))
b = int(input("Enter num 2: "))

if opt == '+':
    print('{} + {} = {}'.format(a, b, a + b))
elif opt == '-':
    print('{} - {} = {}'.format(a, b, a - b))
elif opt == '*':
    print('{} * {} = {}'.format(a, b, a * b))
elif opt == '/':
    if b == 0:
        print("Error: Division by zero!")
    else:
        print('{} / {} = {}'.format(a, b, a / b))
else:
    print("Unsupported operation. Please choose from '+', '-', '*', or '/'")
