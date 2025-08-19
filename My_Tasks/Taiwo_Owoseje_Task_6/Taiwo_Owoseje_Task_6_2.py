# Task 2: Unique Name Collector
print("Welcome to Generative AI Developers Seminar. Kindly enter your names.") # Collecting names of attendees
attendee = set()
attendee.add(input("Enter your name: "))
attendee.add(input("Enter your name: "))
attendee.add(input("Enter your name: "))
attendee.add(input("Enter your name: ")) 
attendee.add(input("Enter your name: ")) 
attendee.add(input("Enter your name: "))
attendee.add(input("Enter your name: "))
attendee.add(input("Enter your name: "))

print("\nattendees:", attendee) # Duplicates completely ignored

# Display names in alphabetical order.
names = sorted(attendee) 
print(f"AI Developers Seminar Attendees.\n********************************\n{names}")