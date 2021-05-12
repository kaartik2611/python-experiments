no_of_subjects = int(input("Enter No of subjects: "))
TW_marks = int(input("Enter Maximum Term Work Marks: "))
subjects = list(map(str, input('Enter Name of Subjects: ').split()))[:no_of_subjects]

marks = [] #  stores all subjects and their respective grades,marks
total = 0  #  avg marks

def grade_gen(marks):
    if marks/TW_marks >= 0.85:
        return 'O'
    if marks/TW_marks >= 0.75:
        return 'A'
    if marks/TW_marks >= 0.6:
        return 'B'
    if marks/TW_marks >  0.4:
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

for i in subjects:
    individual_subject_mark = float(input(f"Enter Marks for Subject {i}: "))
    total += individual_subject_mark
    marks +=[{
        i : { 'marks': individual_subject_mark , 'grade' : grade_gen(individual_subject_mark)}
    }]
    
grade = pointer(marks)/no_of_subjects

print(f'TW Grade : {grade}')
print(f'Average TW marks : {(total*100)/(no_of_subjects*TW_marks)}%')

print(f'data: \n {marks}')