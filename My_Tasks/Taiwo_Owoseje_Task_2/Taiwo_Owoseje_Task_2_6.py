# Task 6 
# Generate a neatly formatted receipt using escape sequences for line breaks

name = input("Enter Customer's full name in CAPITAL: ")
units = int(input("Units consumed (kWh): "))
cost_per_unit = float(input("Cost per unit of electricity used: "))
Total_cost_of_electricity = float(units * cost_per_unit)
print(f"The Total cost of electricity used is {Total_cost_of_electricity}")
# Introduce nextline formatting and center operation
print("\n")
print("*" * 50)
print(name.center(50, " "))
print("RECEIPT".center(50, " "))
print("*" * 50)
print("\n")
# # Introduce \t to format the spacing of the receipt items
print(f"Units of energy consumed in kWh:\t{units}kWh\nCost per unit of Energy used:\t\t₦{cost_per_unit}\nTotal cost of Energy:\t\t\t₦{Total_cost_of_electricity}")
print("\n")
print("*" * 50)
print("THANK YOU FOR YOUR PURCHASE".center(50, " "))
print("*" * 50) 
