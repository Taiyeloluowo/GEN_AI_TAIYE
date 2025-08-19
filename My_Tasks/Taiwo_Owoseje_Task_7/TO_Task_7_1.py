# Task 1: Student Bio Data Storage 
# Collecting student bio-data like (name, age, gender, courses)
bio_data = {} # Storing user bio-data in a dictionary
bio_data["Name"] = input("Enter your name: ")
bio_data["Age"] = input("Enter your age: ")
bio_data["Gender"] = input("Gender: ")
bio_data["Courses"] = input("Enter your courses (comma-separated): ")

bio_data["Courses"] = bio_data["Courses"].split(',') # Storing courses in a list

# Displaying the bio-data
print("\nStudent Bio-Data")
print(f"Name:   \t{bio_data["Name"]}")
print(f"Age:    \t{bio_data["Age"]}") 
print(f"Gender: \t{bio_data["Gender"]}")
print(f"Courses: \t{bio_data["Courses"]}")