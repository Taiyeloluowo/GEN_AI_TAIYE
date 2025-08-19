
# # Task 11 
# Nigerian Currency Converter$

ng_naira = float(input("Amount in Naira(₦): "))
us_dollars = float(input("Exchange rate to US Dollars($): "))
br_pounds = float(input("Exchange rate to British Pounds(£): "))

pound_amount = f"{ng_naira * br_pounds:,}"
dollar_amount = f"{ng_naira * us_dollars:,}"

print("\n")
print("*" * 50)
print("NAIRA CURRENCY CONVERTER".center(50, " "))
print("*" * 50)
print(f"CURRENCY\t\t\tAmount")
print("-----------------------------------------")
print(f"Nigerian Naira(₦):\t\t₦{ng_naira}K\nUS Dollars($):\t\t\t${dollar_amount}\nBritish Pounds(£):\t\t£{pound_amount}")
print("*" * 50)
print("EARN IN DOLLARS, SPEND IN NAIRA".center(50, " "))
print("*" * 50)
