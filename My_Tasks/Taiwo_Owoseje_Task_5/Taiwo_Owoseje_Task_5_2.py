# Task 2: Tuple and Input
best_friends = input("Enter the names of your 5 best friends (seperated only by space): ")
friends = tuple(best_friends.split())
reverse_friends = friends[::-1]
print(reverse_friends)