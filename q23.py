# Get the values in a string where numbers are separated by ','
values = input('Enter integer values to store in the tuple : ')

# Function to get a tuple from a string
def get_tuple(str):
    
    temp_list = str.split(',')                 # Split the string by commas and add to a list

    length = len(temp_list)
    for i in range(0, length):                 # Loop over the list to
        temp_list[i] = int(temp_list[i])       # convert every item to int instead of str (also removes whitespaces)

    t = tuple(temp_list)                       # Construct the tuple from the list
    return t

# Get the required tuple
result_tuple = get_tuple(values)

# Display the tuple
print('The tuple is : ', result_tuple)

# For calculating sum
sum = 0
for item in result_tuple:
    sum += item

print('The sum of all elements is tuple is', sum)

print('The average of all elements in tuple is', sum/len(result_tuple))
