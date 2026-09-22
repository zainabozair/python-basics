print("Hello, World!")
print("Welcome to Python programming.")

# Ask the user to enter their name
name = input("What is your name? ")

# Check if the user pressed Enter without typing a name
if name == "":
    print("Hello! Glad to have you learning Python.")
else:
    # If a name was entered, include it in the greeting
    print("Hello, " + name + "! Glad to have you learning Python.")