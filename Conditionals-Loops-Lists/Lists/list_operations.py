my_list = []

for i in range(5):
    number = int(input("Enter a number: "))
    my_list.append(number)

print("Original list:", my_list)
print("Sorted list:", sorted(my_list))

my_list.sort()
print("Sorted list:", my_list)

my_list.append(30)
print("After adding an element:", my_list)

del my_list[0]
print("After removing an element:", my_list)

my_list.reverse()
print("Reversed list:", my_list)