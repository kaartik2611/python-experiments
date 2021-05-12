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

# Create the object to be pickled
emp1 = Employee('Shahod', 21, 1500)

# Setting the filename
filename = 'emp1_pickle'

# Pickling the object into the file
file = open(filename, 'wb')
pickle.dump(emp1,file)
file.close()
