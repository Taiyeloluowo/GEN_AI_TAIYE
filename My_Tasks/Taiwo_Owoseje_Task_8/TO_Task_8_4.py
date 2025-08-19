# Task 4
student = {}
name = input("Enter your name: ")
age = int(input("Enter your age: "))
student["name"] = name
student["age"] = age
scores = [70, 85, 90]
student["scores"] = scores
average_score = sum(scores)/len(scores)
passed = (average_score >= 50)
student["passed"] = passed
teenager = (age >= 13) and (age <= 19)
student["teenager"] = teenager 
print(f"\tStudent Record\nName: \t\t{name}\nAge: \t\t{age}\nScore: \t\t{scores}\nPassed: \t{passed}\nTeenager: \t{teenager}")