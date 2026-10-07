# Tuple containing the twelve months
months = ("January", "February", "March", "April",
          "May", "June", "July", "August",
          "September", "October", "November", "December")

# Print the first and last month
print("First month:", months[0])
print("Last month:", months[-1])

try:
    months[0]="NewMonth"
except Exception as error:
    print("Tuples are immutable, error:", error)

# create a dictionary
students = {
    "Adam": 90,
    "Ana": 85,
    "Mary": 95
}

students["John"]=88    # Add new student
students["Ana"] = 92   # change the grade

# Print each student's name and grade
for name, grade in students.items():
    print(name, ":", grade)
