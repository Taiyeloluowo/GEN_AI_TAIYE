# Task 4: Tuple Unpacking
first_name = input("Enter your first name: ")
age = input("Enter your age: ")
favcolor = input("Enter your favourite color: ")
htown = input("Enter your hometown: ")
details = first_name, age, favcolor, htown
print(type(details))
print(details)
print("\n".join(details))
print(f"Firstname: \t{first_name} \nAge: \t\t{age} \nFavourite colour: {favcolor} \nHometown: \t{htown}")