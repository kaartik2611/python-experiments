# 2 Write a menu-driven program in python to implement Calculator

while True:   
    print('Welcome to the Menu Driven Program')
    print('1.Perform Addition')
    print('2.Perform Subtraction')
    print('3.Perform Multiplication')
    print('4.Perform Division')
    print('5.EXIT')
    try:     # adding exceptions if number is not string
        choice = int(input("Enter Your Choice: "))
    except ValueError:
        print("Try entering a valid number")
        break

    if choice == 1:
        n1 = float(input("Enter n1: "))
        n2 = float(input("Enter n2: "))
        n3 = n1 + n2
        print(" {} added to {} is {}".format(n1,n2,n3)) # for format reference :https://www.geeksforgeeks.org/python-format-function/
        print("")

    elif choice == 2:
        n1 = float(input("Enter n1: "))
        n2 = float(input("Enter n2: "))
        n3 = n1 - n2
        print("{} subtracted by {} is {}".format(n1,n2,n3))
        print("")

    elif choice == 3:
        n1 = float(input("Enter n1: "))
        n2 = float(input("Enter n2: "))
        n3 = n1 * n2
        print("{} multiplied by {} is {}".format(n1,n2,n3))
        print("")

    elif choice == 4:
        n1 = float(input("Enter n1: "))
        n2 = float(input("Enter n2: "))
        try:
            n3 = n1 / n2
            print("{} divided by {} is {}".format(n1,n2,n3))
            print("")
        except ZeroDivisionError:
            print("Unable to divide by zero.")
            print('')

    elif choice==5 :
        print("Thanks for using.")
        break

    else:
        print("Wrong Choice")
        print("Please try again")
        print("")