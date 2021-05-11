import numpy as np 
print("Enter the data of matrix 1")
arr1 = np.array([[int(x) for x in input(f"Enter the value for {i+1}th row of matrix1: ").split()][:3] for i in range(3)])

print("Enter the data of matrix 2")
arr2 = np.array([[int(x) for x in input(f"Enter the value for {i+1}th row of matrix2: ").split()][:3] for i in range(3)])

sum = np.add(arr1,arr2)
print(f'The sum of the matrices are : \n {sum}')

product = np.matmul(arr1,arr2)
print(f'The product of the matrices are : \n {product}')

