# Task 3: Simulate a football match ticket system
seat_num = set(range(1, 51)) # Store all seat numbers (1 to 50) in a set.

# Ask users to "book" a seat by entering the number.
book1 = int(input("Enter your booking number: "))
book2 = int(input("Enter your booking number: "))
book3 = int(input("Enter your booking number: "))
book4 = int(input("Enter your booking number: "))
book5 = int(input("Enter your booking number: "))

# Remove booked seats from the set.
seat_num.remove(book1)
seat_num.remove(book2)
seat_num.remove(book3)
seat_num.remove(book4)
seat_num.remove(book5)

# Show remaining seats after each booking.
print(seat_num)