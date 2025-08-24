# Create a Unique Voters Registration System**
# - Ask for voter names and store in a set.
# - If a voter tries to register twice, display a warning.
# - After registration, display the total number of unique voters.

print("\nList of Selected Voters.")
voter1 = input("Enter your name: ")
voter2 = input("Enter your name: ")
voter3 = input("Enter your name: ")
voter4 = input("Enter your name: ")
voter5 = input("Enter your name: ")

# voters = (voter_1, voter_2, voter_3, voter_4, voter_5)
voters = set() # Storing voters in a set 
for voter in [voter1, voter2, voter3, voter4, voter5]:
    if voter in voters: 
        print(f"warning: {voter} has already registered.") # Display a warning, if a voter tries to register twice.
    else: 
        voters.add(voter)

print("\nTotal number of unique voters: ", len(voters)) # Display the total number of unique voters.
print("Voters list:", ", ".join(voters))