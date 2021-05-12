def combine(str1, str2):
    return str1 + ' ' + str2

test1 = 'Hello'
test2 = 'World'

print('To Demonstrate Positional Arguments : ')

# The output will be different because the order of arguments are changed i.e, they
# are positional and their position in the function call determines the output
print(combine(test1, test2))
print(combine(test2, test1))
print()

print('To Demonstrate Keyword Arguments : ')

# The output will be same even though their positions are changed
# because the function was called with the parameters/keywords
# For eg, str1/2 are parameters/keywords and test1/2 are the arguments

print(combine(str1=test1, str2=test2))
print(combine(str2=test2, str1=test1))
