# Student Record**
# - Create an empty dictionary called student.
# - Ask the user to input their name and age, then store them in the dictionary.
# - Add a list of scores (e.g., [70, 85, 90]) to the dictionary.
# - Use a comparison operator to check if the student has passed (average score >= 50). Save the result (True/False) in the dictionary under the key "passed".


student = {}
items_list = ['Name', 'Age', 'Scores']
name = input('Enter name here ')
age = int(input('Enter your age here '))

student['scores'] = [65, 70 ,85]
if sum(student['scores']) / len(student['scores']) >= 50:
    print('Passed')
else:
    print('Failed')