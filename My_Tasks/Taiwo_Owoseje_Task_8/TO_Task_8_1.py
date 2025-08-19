# Task 1
# Explain each output of the program below

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
# Collection of values from a user and changing it to an integer type. It shows the operation of typecasting which is converting a value from one data type to another

print(f"{num1} == {num2} : {num1 == num2}")
# Using f-string formatting and equal-to sign to display equality between two variables along with the values themselves.

print(f"{num1} != {num2} : {num1 != num2}")
# Using f-string formatting and not-equal-to sign to display inequality between two variables along with the values themselves.

print(f"{num1} > {num2} : {num1 > num2}")
# Using f-string formatting and greater-than sign to display comparison between two variables along with the values themselves.

print(f"{num1} < {num2} : {num1 < num2}")
# Using f-string formatting and less-than sign to display comparison between two variables along with the values themselves.

# Task 1_2
# Scenario 1 - Comparing expected number of items to be produced to the actual number of items produced
# Scenario 2 - Comparing expected cost of production to actual cost of production
# Scenario 3 - Comparing expected sales revenue to actual sales revenue

# Task 1_3

# Scenario 1 - Comparing expected number of items to be produced to the actual number of items produced
expected_production = 300
actual_production = int(input("Enter actual number of items produced: "))

print(f"Expected production: {expected_production} == Actual production: {actual_production} : {expected_production == actual_production}")