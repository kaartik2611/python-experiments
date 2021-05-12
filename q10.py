# Write a python program to perform exception handling using try, except, finally, else, 
# assert and raise

x=1

try : 
    print(x)
except NameError:
    print('the variable x is not defined.')
else:
    print("Nothing went wrong")
finally:
    print('the try except block has been executed')

try : 
    print(y) # variable not initialized
except NameError:
    print('the variable y is not defined.')
else:
    print("Nothing went wrong")
finally:
    print('the try except block has been executed')

natural_number = int(input("Enter a natural number:"))

if natural_number <= 0:
    raise TypeError("Natural numbers are supposed to greater than 0.")
else:
    print("Entered number is a natural number.")
