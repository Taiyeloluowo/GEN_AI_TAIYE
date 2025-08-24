# Simulated USSD Menu Interaction
#  - You are to design a mock USSD interface for a mobile service.
#  - Requirements:
#    1. When the user runs the program, display a welcome screen with a Nigerian context greeting.
#    2. Ask the user to "dial" a USSD code (e.g., *123#) and store it in a variable.
#    3. Print a menu with at least 3 options (e.g., "Check Balance", "Buy Airtime", "Buy Data") using newline escape sequences `(\n)` for formatting.
#    4. Ask the user to choose an option (1, 2, or 3) and store their choice in a variable.
#    5. Use f-strings and/or concatenation to display a confirmation message showing the selected option.
#    6. Ask for an amount (if applicable) and store it as a number using type casting.
#    7. Display a final message summarizing the transaction.


# 1. Welcome screen with Nigerian greeting
print("*** Welcome to 9mobile Naija Mobile Service ***")

# 2. Ask user to "dial" a USSD code
ussd_code = input("Please dial your USSD code *123#: ")
balance = 2000

# 3. Print menu with newline formatting
while True:
    print("\nMenu:")
    print("1. Check Balance\n2. Buy Airtime\n3. Buy Data\n4. Exit")

# 4. Ask user to choose an option
    choice = input("Select an option (1, 2, 3 or 4): ")

    if choice == "1":
        print(f"Your balance is ₦{balance}")
    elif choice == "2":
# 6. Ask for an amount if applicable
        amount = float(input("Enter Airtime amount: "))
        balance += amount
        print(f"Airtime purchase successful. New balance: {balance:.2f}")
    elif choice == "3":
        data = float(input("Enter Data amount: "))
# 5. Display confirmation using f-strings
        print(f"₦{data:.2f} data purchase successful.")
    elif choice == "4":
        print("Thank you for using 9mobile Naija Mobile!")
        break
# 7. Final message
    else:
        print("Invalid option. Try again.")