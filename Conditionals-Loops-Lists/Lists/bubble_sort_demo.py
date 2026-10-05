my_list = [64, 25, 12, 22, 11]
print("Original list:", my_list)

# Outer loop controls each pass through the list
for i in range(len(my_list)):
    #inner loop comapers neighbour
    for j in range(len(my_list)-1):
         # Swap them if they are in the wrong order
        if my_list[j] > my_list[j + 1]:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
           
    print("Pass", i + 1, ":", my_list)  # Show the list after each pass

print("Final Sorted list:", my_list)
