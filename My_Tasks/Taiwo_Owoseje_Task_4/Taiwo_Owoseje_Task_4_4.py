# Task 4: Name Organizer
name = input("Enter 5 names, separated by spaces: ")
name_sp = name.lower().split(" ")
name_sp.sort()
print(name_sp)
[print(f"{name}") for name in name_sp]