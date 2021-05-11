from math import factorial


# Function for fibonacci
def fibo(num):
    if num <= 1:
        return num
    else:
        return (fibo(num-1) + fibo(num-2))

# Function for Multiplication Table
def mult_table(num, rows):
    for i in range(1, rows+1):
        print(f'{num} x {i} = {num*i}')

# Function for Pascal's triangle
def pascal(rows):
    for i in range(rows):                                                  # To print spaces before
        print(' ' * (rows-i), end='')                                      # first item in row

        for j in range(i+1):
            temp = factorial(i) // (factorial(j) * factorial(i-j))         # To calculate the terms using nCr formula
            print(temp, end=' ')                                           # and display it
        
        print()                                                            # For new line after every row

print('"f" for Fibonacci, "m" for Multiplication Table, "p" for Pascal\'s traingle')
func = input('Enter which function to perform : ')

if func == 'f':
    temp = int(input('Enter the term : '))
    for i in range(1, temp+1):
        print(fibo(i))

elif func == 'm':
    num = int(input('Enter the number : '))
    rows = int(input('Enter the number of rows : '))
    mult_table(num, rows)

elif func == 'p':
    temp = int(input('Enter the number of rows : '))
    pascal(temp)

else:
    print('Enter a valid option')
