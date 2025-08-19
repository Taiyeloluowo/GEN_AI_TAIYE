# Task 6
# collect candidate details
candidate = input("Enter your full name (first name + last name): ")
age = int(input("Enter your age: "))
school_choice = input("Is your first school of choice UNILAG? yes or no: ")
course = input("Enter your course of choice: ")
utme_score = int(input("Enter your UTME score: "))
qualified = (utme_score >= 200)
dept_cut_off = (utme_score >=200) and (utme_score <= 320)
o_level_requirements = input("Do you have five (5) credit passes at one sitting in relevant O'Level subjects, including English Language and Mathematics? yes or no: ")
# ascertain eligibility
eligible = (age >= 16) and (school_choice == "yes") and (qualified == True) and (o_level_requirements == "yes") and (dept_cut_off == True)
# Display candidate details
print(f"\n\tSTUDENT REQUIRED DETAILS\nCandidate: {candidate}\nAge: {age}\nCourse of study: {course}\nUTME score: {utme_score}\nIs UNILAG your first choice: {school_choice}\nDo you have at least five credits in your O'level result: {o_level_requirements}\nDepartmental Cut-Off Mark: {dept_cut_off}")
# confirm if candidate meets all requirements or not
admission = {True: "Congratulations, you have met all the requirements and have been offered unconditional admission into UNILAG", False: "Sorry, you did not meet the requirements for the admission"}
# Display outcome of required details
print(f"\n\t\t\tADMISSION STATUS: \nDear {candidate}, {admission[eligible]} to study {course}.")