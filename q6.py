# Write a python program to search an element in 1D Array.

lst = list(map(int,input("Enter the numbers in the list : ").split())) # add numbers directly into the list by using split and map method
n = int(input("Enter Number to be searched: "))
for i in lst:
    if n in lst:
        print('{} is present in the list:{}.'.format(n,lst))
        break
    else:
        print('{} is not present in the list:{}.'.format(n,lst))
        break