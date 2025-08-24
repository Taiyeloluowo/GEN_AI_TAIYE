# Unique Members Registration**
# - Ask the user to enter three names separated by commas.
#    - Convert them to a set to ensure uniqueness.
#    - Create a dictionary where each name is a key and its length is the value.
# - Requirements:
#    - Use `.split(",")` and `set()` to remove duplicates.
#    - Use dictionary comprehension `{name: len(name) for name in set_of_names}`.


print("Kindly enter three names.") # Ask the user to enter three names separated by commas.
names = input("Enter 3 names '(separated by comma)': ")

# Convert them to a set to ensure uniqueness
name = ()
names_set =set(n.strip() for n in names.split(","))
print(names_set)

# Create a dictionary where each name is a key and its length is the value.
print("\nThe names and their lengths are:")
for name in names_set:
    print({name: len(name)})