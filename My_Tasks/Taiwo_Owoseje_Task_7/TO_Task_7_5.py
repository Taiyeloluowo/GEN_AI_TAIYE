# Task 5: Contact Quick Lookup
# Store three names and their phone numbers in two separate tuples.
names = ()
phone_numbers = ()

print("Available Contacts for a Quick Lookup")
names = ("Ayomide", "Divine", "Ayooluwa")
print(f"The names are: {names}")

phone_numbers = ("08101143265", "07067331744", "08134567893")
print(f"The phone numbers are: {phone_numbers} ")

# Create a dictionary from them using `dict(zip(...))`.
# Use `zip()` and d`ict()` to combine tuples.
print("The following are the names of customers and their individual phone numbers:")
contact = dict(zip(names, phone_numbers))
print(contact)

# Ask the user for a name and display the corresponding number (or an error message).
# Use `.get()` for safe retrieval.
print(contact.get(input("\nEnter a name: "), "an error message"))