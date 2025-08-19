# Task 2_1
name = input("Enter your name: ")               # collects input for the name variable
age = int(input("Enter your age: "))            # collects input for the age variable
score = int(input("Enter your test score: "))   # collects input for the score variable

eligibility = (age < 18) and (score > 70)       # using comparison operators to show the boolean value of the "eligibility" variable
print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")    # display the variable item and values

'''
The code aims to collect input for important variables which are needed to confirm the eligibility of a user.
'''

# Task 2_2
print("\tFederal Government Scholarship Key Eligibility Requirements")
name = input("Enter your name: ")
citizenship = input("Are you a Nigerian citizen? yes or no: ").strip().lower()
enrollment = input("Are you a REGISTERED, FULL-TIME UNDERGRADUATE STUDENT in a recognized Nigerian university? yes or no: ").strip().lower()
other_scholarships = input("Are you currently receiving any other scholarship from an entity in the Oil and Gas industry, whether national or international? yes or no: ").strip().lower()
academic_qualification = input("Do you have FIVE DISCTINCTIONS (As and Bs) in relevant subjects in your WAEC/WASSCE (May/June) exams, including English and Mathematics? yes or no: ").strip().lower()
eligibility = (citizenship == "yes") and (enrollment == "yes") and (other_scholarships == "no") and (academic_qualification == "yes")
print(f"Candidate: {name}\nEnrollment: {enrollment}\nScholarship: {other_scholarships}\nAcademic Qualifictaion: {academic_qualification}\nEligibility: {eligibility}")