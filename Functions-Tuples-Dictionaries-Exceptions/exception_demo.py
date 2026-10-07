# Divides two numbers safely
def safe_divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# Test successful division
try:
    result = safe_divide(10, 2)
    print("Result:", result)
except ValueError as error:
    print("Error:", error)
finally:
    print("Division operation completed")


# Test division by zero
try:
    result = safe_divide(10, 0)
    print("Result:", result)
except ValueError as error:
    print("Error:", error)
finally:
    print("Division operation completed")

# Demonstrate a generic exception
try:
    number = int("hello")
except Exception as error:
    print("Generic error:", error)