# # Task 10
# School Fees Breakdown

name = input("What is your school name: ")
fee = float(input("How much is the Tuition fee: "))
Hostel = float(input("How much is the Hostel fee: "))
feeding = float(input("How much is the feeding fee? "))
Total_school_fee = float(fee + Hostel + feeding)
print(f"The Total cost of the school fees is {Total_school_fee}")

print("\n")
print("*" * 50)
print(name.center(50, " "))
print("RECEIPT".center(50, " "))
print("*" * 50)
print("\n")

print(f"Tution fee:\t\t\t₦{fee}K\nHostel fee:\t\t\t₦{Hostel}K\nFeeding fee:\t\t\t₦{feeding}K\n\nTotal School Fees:\t\t₦{Total_school_fee}K")
print("\n")
print("*" * 50)
print("THANK YOU FOR YOUR PURCHASE".center(50, " "))
print("*" * 50)