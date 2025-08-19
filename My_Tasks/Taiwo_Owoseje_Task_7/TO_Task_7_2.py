# Task 2: Super Market Price List
items = {} # Storing items in a dictionary
print("The following are the available items available for purchase.")
item_1 = ("Sugar")
item_2 = ("Indomie")
item_3 = ("Groundnut")
item_4 = ("Biscuit")
item_5 = ("Sweet")

items = (item_1, item_2, item_3, item_4, item_5)
print(items)

prices = {} # Storing prices in a dictionary
print("\nPlease enter the prices of the above listed items.")
price_1 = float(input("Enter the price for Sugar: "))
price_2 = float(input("Enter the price for Indomie: "))
price_3 = float(input("Enter the price for Groundnut: "))
price_4 = float(input("Enter the price for Biscuit: "))
price_5 = float(input("Enter the price for Sweet: "))

price_list = {price_1, price_2, price_3, price_4, price_5}

# Displaying all items
print(f"\nAvailable items available for purchase and their prices:\n{item_1}:\t\t#{price_1: ,.2f}k\n{item_2}:\t#{price_2: ,.2f}k\n{item_3}:\t#{price_3: ,.2f}k\n{item_4}:\t#{price_4: ,.2f}k\n{item_5}:\t\t#{price_5: ,.2f}k ")

# Allowing user to update the price of an item
price_update = float(input("\nPlease enter a new price for Groundnut: "))
price_list.update({price_update,})
price_3 = price_update 
print(f"The updated price for Groundnut is now: #{price_update: ,.2f}k")
print("\nThe updated prices for all available items are:")
print(f"{item_1}: \t\t#{price_1: ,.2f}k\n{item_2}: \t#{price_2: ,.2f}\n{item_3}: \t#{price_update: ,.2f}k\n{item_4}: \t#{price_4: ,.2f}k\n{item_5}: \t\t#{price_5: ,.2f}k")