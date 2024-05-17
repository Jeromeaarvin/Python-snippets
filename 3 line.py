try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    print("Addition: " + str(num1 + num2))
    print("Subtraction: " + str(num1 - num2))
    print("Multiplication: " + str(num1 * num2))

except ValueError:
    print("Please enter valid integers.")
