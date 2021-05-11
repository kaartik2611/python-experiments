# Enter non-zero positive values and ensure start <= end

# Function to generate list
def get_list(start, end, interval):
    return list(range(start, end, interval))

# Get the required values
s = int(input('Enter the starting element of the list : '))
e = int(input('Enter the ending element of the list : '))
i = int(input('Enter the interval between elements : '))

# Generate the list
result = get_list(s, e, i)

# Display it
print('The list is : ')
print(result)
