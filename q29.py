marks_list = list(map(int,input("Enter Marks: ").split()))
max_marks = int(input("Enter Maximum Marks for One Exam: "))
print(f"Total Marks: {sum(marks_list)}")
print(f"Percentage: {sum(marks_list)*100/(len(marks_list)*max_marks)}%")