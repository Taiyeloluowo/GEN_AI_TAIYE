
# # Task 12
# USSD Interface Simulation

# 1. Welcome screen with Nigerian greeting
print("*** Welcome to 9mobile Naija Mobile Service ***")

# 2. Ask user to "dial" a USSD code
ussd_code = input("Please dial your USSD code (e.g., *123#): ")

# 3. Print menu with newline formatting
print("\nMenu:")
print("1. Check Balance\n2. Buy Airtime\n3. Buy Data")

# 4. Ask user to choose an option
choice = input("Select an option (1, 2, or 3): ")

# 5. Display confirmation using f-strings
print(f"\nYou selected option {choice}.")

# 6. Ask for an amount if applicable
amount = float(input("Please indicate an amount for option 2 or 3: ₦"))

# 7. Final message
print(f"₦{amount} purchase successful. Thank you for using 9mobile Naija Mobile!")