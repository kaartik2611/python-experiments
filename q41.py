# Implement a system for exam department that accept student details along with 
# marks and display the Grade obtained by the student.
student_db = {}
subjects = ['COA','CNN','Maths','Python','OS']
total_marks = 100
def grade_gen(marks):
    if marks/total_marks >= 0.85:
        return 'O'
    if marks/total_marks >= 0.75:
        return 'A'
    if marks/total_marks >= 0.6:
        return 'B'
    if marks/total_marks >  0.4:
        return 'C'
    else : 
        return 'D'

def pointer(marks):
    grade_counter = 0
    for i in marks:
        for j in i.values():
            if j['grade'] == 'O':
                grade_counter += 10.0
            
            if j['grade'] == 'A':
                grade_counter += 8.5
            
            if j['grade'] == 'B':
                grade_counter += 7.5
            
            if j['grade'] == 'C':
                grade_counter += 6
            
            if j['grade'] == 'D':
                grade_counter += 4
    return grade_counter

while True:
    print("Student DataBase")
    print("1.Add Student Details")
    print("2.Display Student Grade")
    print("3.Display all Student List")
    print("4.Exit the Program")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input('Enter Student Name: ')
        if name in student_db:
            print('')
            print('Cannot add another user with same name.')
        else:
            marks= []
            student_db[name] = marks
            for i in subjects:
                subject_mark = float(input(f"Enter Marks for Subject {i}: "))
                marks +=[{
                    i : { 'marks': subject_mark , 'grade' : grade_gen(subject_mark)}
                }]
        print("")

    elif choice == 2:
        search = input('Enter name of Student:')
        if search not in student_db:
            print('Student details does not exist.')
            print('For student List, choose option 3.')
        else:
            data  = student_db.get(search)
            grade = pointer(data)/5   
            print(f'The grade of {search} is {grade}')         
        print("")
    
    elif choice == 3:
        print(student_db.keys())
        print("")
    
    elif choice == 4:
        print("Thanks for using.")
        break
    
    else:
        print("Wrong Choice")
        print("Please try again")
        print("")