
try:
    quote = input("What is your favourite quote: ")
    print(f"\"{quote.title()}\"")
except ValueError:
    print("Error: Invalid Input")