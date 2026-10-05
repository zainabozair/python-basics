numeric_grade=int(input("Please enter numeric grade 0-100: "))
if numeric_grade>=90:
    print("Your grade is: A")
elif numeric_grade >= 80:
    print("Your grade is: B")
elif numeric_grade >= 70:
    print("Your grade is: C")
elif numeric_grade >= 60:
    print("Your grade is: D")
else:
    print("Your grade is: F")

print("Congratulations!" if numeric_grade >= 70 else "Work hard and try again!")
