class Student:
    def __init__(self, name, age, phy, chem, math):
        self.name = name
        self.age = age
        self.phy = phy
        self.chem = chem
        self.math = math
    
    def get_grade(self):
        self.avg = (self.phy + self.chem + self.math)/3
        if self.avg >= 90:
            return 'A'
        elif self.avg >= 80:
            return 'B'
        elif self.avg >= 70:
            return 'C'
        elif self.avg >= 60:
            return 'D'
        elif self.avg >= 35:
            return 'E'
        else:
            return 'F'


print()
name = input("Enter Student's name : ")
age = int(input("Enter Student's age : "))
phy = int(input("Enter Student's mark in Physics : "))
chem = int(input("Enter Student's mark in Chemistry : "))
math = int(input("Enter Student's mark in Maths : "))
print()
stud = Student(name, age, phy, chem, math)
print("The Student's grade is", stud.get_grade())

