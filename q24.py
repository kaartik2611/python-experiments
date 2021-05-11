# Create dictionaries for every employee

emp1 = { 'name' : 'Alvin', 'age' : 19, 'salary' : 69000 }
emp2 = { 'name' : 'Rohini', 'age' : 18, 'salary' : 60000 }
emp3 = { 'name' : 'Payal', 'age' : 19, 'salary' : 65000 }
emp4 = { 'name' : 'Viren', 'age' : 20, 'salary' : 42000 }

# Nested dictionary where the id of emp is related to dictionary containing employee's data
employees = {
    'ID01' : emp1, 'ID02' : emp2, 'ID03' : emp3, 'ID04' : emp4,
}

# Get required id from user
id = input('Enter employee ID : ').upper()

# Display data of employee related to that id
print('Name of the employee is', employees[id]['name'])
print('Age of the employee is', employees[id]['age'])
print('Salary of the employee is', employees[id]['salary'])
