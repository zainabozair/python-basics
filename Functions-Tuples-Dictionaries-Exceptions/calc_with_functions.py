# Adds two numbers
def add(a, b):
    return a + b


# Subtracts the second number from the first
def subtract(a, b):
    return a - b


# Multiplies two numbers
def multiply(a, b):
    return a * b


# Divides the first number by the second
def divide(a, b):
    return a / b


# Chooses the correct operation
def calculate(a, b, op):
    if op == "+":
        return add(a, b)
    elif op == "-":
        return subtract(a, b)
    elif op == "*":
        return multiply(a, b)
    elif op == "/":
        return divide(a, b)
    else:
        return "Invalid operation"


# Get input from the user
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")

    result = calculate(a, b, op)
    print("Result:", result)

except ValueError:
    print("Error: Please enter valid numbers.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")