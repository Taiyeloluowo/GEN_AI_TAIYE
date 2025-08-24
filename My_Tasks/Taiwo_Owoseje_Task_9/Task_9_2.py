# Name Organizer**
# - Ask the user to enter 5 names (separated by spaces).
# - Convert all names to lowercase.
# - Sort the list alphabetically.
# - Display them one name per line.
#   -Tips: use `range()`,`sort()`, `for`, `in`, `split()`, `len()`,`lower()` 


# Collect names from user
name = input("Enter 5 names, separated by spaces: ")
# convert them to lower case and split
name_sp = name.lower().split(" ")
#sort names in alphabetical order
name_sp.sort()
print(name_sp)
# print names, one name per line
for name in name_sp:
    print(name)