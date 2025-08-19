# Task 6 Attendance Tracker
weekdays = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
yearmonth = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
name = input("Enter Student Name: ")
gender = input("Enter Gender: ")
course = input("Enter Course Track: ")
month = int(input("Enter Current Month in number(1-12): ")) - 1
day = int(input("Enter Current Day in number(1-7): ")) - 1

print("Days of the week", weekdays)
print("Months of the year", yearmonth)
print(f'''
    Student Name:   {name}
    Student Gender: {gender}
    Course Track:   {course}
    Current Month:  {yearmonth[month]}
    Current Day:    {weekdays[day]}
''')