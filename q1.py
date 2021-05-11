# Write a program in python to accept student details and marks , calculate the 
# percentage and check if the student is eligible for the admission

student_name = input("Enter your name: ")
roll_no = input("Enter Your Roll Number: ")
marks = float(input("Enter Your 12th Percentage: "))
if marks >= 40 :
    print("You are eligible for admission.")
else:
    print("You are not eligible for admission.")