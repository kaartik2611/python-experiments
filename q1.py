# Write a program in python to accept student details and marks , calculate the 
# percentage and check if the student is eligible for the admission

student_name = input("Enter your name: ")
roll_no = input("Enter Your Roll Number: ")
marks = list(map(int,input("\nEnter the marks in each subject : ").strip().split()))[:5]
print(marks)
percentage = sum(marks)/5
if percentage >= 40 :
    print("You are eligible for admission.")
else:
    print("You are not eligible for admission.")