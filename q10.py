x=1

print()
print('=' * 30)
print()

try : 
    print(x)
except NameError:
    print('The variable x is not defined.')
else:
    print("Nothing went wrong")
finally:
    print('The try except block has been executed')

print()
print('=' * 30)
print()

try : 
    print(y)
except NameError:
    print('The variable y is not defined.')
else:
    print("Nothing went wrong")
finally:
    print('The try except block has been executed')

print()
print('=' * 30)
print()

natural_number = int(input("Enter a natural number : "))

if natural_number <= 0:
    raise TypeError("Natural numbers are supposed to greater than 0.")
else:
    print("Entered number is a natural number.")

print()
print('=' * 30)
print()

a = 4
b = 0
print(f'Value of a is {a}')
b = int(input('Enter value of b : '))

assert b != 0, "Cannot divide a number by zero"
print ("The value of a / b is : ")
print (a / b)
