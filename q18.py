import numpy as np 
arr = np.array([[int(x) for x in input(f"Enter the value for {i+1}th row of matrix: ").split()][:3] for i in range(3)])

determinant = round(np.linalg.det(arr))
try:
    inverse = np.linalg.inv(arr)
    print(f'The inverse of the above matrix is \n {inverse}')
except np.linalg.LinAlgError:
    print("inverse of matrix doesnt exist because given matrix is a singularity matrix (det|A| = 0)")

print(f'The determinant of the above matrix is {determinant}.')
