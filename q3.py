# Write a menu driven program in python to print Factorial, multiplication table and Fibonacci series

from math import factorial

while True:
    print('Welcome to the Menu Driven Program')
    print('1.Perform Factorial')
    print('2.Display Multiplication Table')
    print('3.Display Fibonacci Series')
    print('4.EXIT')
    try:       # adding exceptions if number is not string
        choice = int(input("Enter Your Choice: "))
    except ValueError:
        print("Try entering a valid number")
        break
    
    if choice == 1:
        n = int(input("Find factorial of: "))
        print('the factorial of {} is {}'.format(n,factorial(n))) # for format reference :https://www.geeksforgeeks.org/python-format-function/
        print('')

    elif choice == 2:
        n = int(input("Display Multiplication Table of: "))
        print('The Multiplication table of {} is'.format(n))
        for i in range(1,11):
            print("{}*{}={}".format(n,i,n*i))
        print('')

    elif choice == 3:
        n = int(input("Display Fibonacci series till: "))
        n1,n2 =0,1
        counter = 0
        while n > counter:
            print(n1)
            n3 = n1 + n2
            n1 = n2
            n2 = n3
            counter += 1
        print('')

    elif choice == 4 :
        print("Thanks for using.")
        break
    
    else:
        print("Wrong Choice")
        print("Please try again")
        print("")
