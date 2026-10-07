
# Greets the user based on whether a name is provided
def greet_user(name):
    if name == "":
        print("Hello! Welcome!")
    else:
        print("Hello,", name + "! Welcome!")

name = input("Enter your name: ")
greet_user(name)


# add two numbers
def add_two_numbers(a, b):
    return a+b

result = add_two_numbers(1, 1)
print(result)

# Checks if a number is even
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print("4 is even:", is_even(4))
print("5 is even:", is_even(5))