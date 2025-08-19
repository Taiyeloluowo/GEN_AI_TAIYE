# Task 5 
# Collect daily market report details at a local market and display the result with f-string formatting.

market = input("Enter Market name: ")
traders = input("Enter Number of traders: ")
revenue = float(input("Enter daily revenue in naira: ₦"))
daily_revenue = f"{revenue:,}"
print(f"The Daily Market report for {market} market: \n{traders} number of traders were in {market} market today; \nA total value of ₦{daily_revenue} was exchanged.")
