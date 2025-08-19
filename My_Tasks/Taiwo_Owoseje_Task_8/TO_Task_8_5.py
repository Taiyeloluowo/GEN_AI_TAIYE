# Task 5
store = {"Book": 10, "Pen": 20, "Bag": 5}
purchase_item = input("What do you want to buy? ")
purchase_qty = int(input("How many do you want to buy? "))
print("Before Purchase: ", store)
store[purchase_item] -= purchase_qty
print("After purchase: ", store)