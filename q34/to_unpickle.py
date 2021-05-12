import pickle


# Define the class
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def display(self):
        print('Name    :', self.name)
        print('Age     :', self.age)
        print('Salary  :', self.salary)

# Set the filename
filename = 'emp1_pickle'

# Unpickling the object from the file 
picklefile = open(filename, 'rb')
emp1 = pickle.load(picklefile)
picklefile.close()

# Showing the type and contents of the object
print(type(emp1))
emp1.display()
