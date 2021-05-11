#  Write a python program to accept two matrices and find their tanspose, addition and 
# product. 

# Note : Install numpy using cmd
# pip install numpy 

import numpy as np 

dimension = int(input('Enter dimension of Matrix: '))

print("Enter the data of matrix 1")

# Entering data in matrix row-wise using for loop and list comprehension.
arr1 = np.array([[int(x) for x in input(f"Enter the value for {i+1}th row for matrix1: ").split()][:dimension] for i in range(dimension)])
 
print("Enter the data of matrix 2")
arr2 = np.array([[int(x) for x in input(f"Enter the value for {i+1}th row for matrix2: ").split()][:dimension] for i in range(dimension)])
print("Matrix 1:")
print(arr1)
print("Matrix 2:")
print(arr2)

while True:
    print("1.Find transpose of both matrices.")
    print("2.Find sum of both matrices.")
    print("3.Find product of both matrices.")
    print('4.Exit')
    choice = int(input('Enter Choice: '))

    if choice == 1:
        print(f'The transpose of matrix 1 is : \n {arr1.transpose()}')
        print(f'The transpose of matrix 2 is : \n {arr2.transpose()}')
    
    if choice == 2:
        print(f'The sum of the matrices are : \n {np.add(arr1,arr2)}')

    if choice == 3:
        print(f'The product of the matrices are : \n {np.matmul(arr1,arr2)}')

    if choice == 4 :
        print("Thanks for using.")
        break
    
    else:
        print("Wrong Choice")
        print("Please try again")
        print("")