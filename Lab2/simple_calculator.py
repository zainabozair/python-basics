# Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask which operation to perform
operation = input("Choose an operation (+, -, *, /): ")
if operation == "+":
    n= num1 + num2
    print(num1, operation, num2, "=", n)
elif operation == '-':
    n= num1 - num2
    print(num1, operation, num2, "=", n)
elif operation == "*":
    n = num1 * num2
    print(num1, operation, num2, "=", n)
elif operation == "/":
    if num2 == 0:  # considering the error with zero
        print("Cannot divide by zero.")
    else:
        n = num1 / num2
        print(num1, operation, num2, "=", n)
else:
    print("Invalid operation")


