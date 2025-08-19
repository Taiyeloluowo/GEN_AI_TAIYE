# Task 3: Days and Activities Pairing
print("\nDays of the Week") 
days_of_the_week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "saturday") # Store days of the week in a tuple.
print(days_of_the_week)

print("\nKindly fix one activity each for the following listed days of the week.") # Ask user to input an activity for three specific days
activity_1 = input("Enter an activity for Sunday: ")
activity_2 = input("Enter an activity for Wednesday: ")
activity_3 = input("Enter an activity for Saturday: ")
activities = (activity_1, activity_2, activity_3)

print("\nThe activities for the week are:")
activities_for_the_week = {
    "Sunday": activity_1,
    "Monday": "No activity",
    "Wednesday": activity_2,
    "Thursday": "No activity",
    "Friday": "No activity",
    "Saturday": activity_3
}
for key, value in activities_for_the_week.items():
    print(f"{key}: {value}")

# Print the dictionary
print("\nActivities for the Week.")
days_activities = dict(zip(days_of_the_week, activities))
print(days_activities)