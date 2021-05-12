# Write a python program to implement Byte Array, Range, Set and STRING Functions

# Byte Array

num = 5
string = 'ByteArray'
lst = [1,2,3,4,5]
ba_num = bytearray(num)
print(ba_num)
ba_str = bytearray(string, 'utf-8')
print(ba_str)
ba_list = bytearray(lst)
print(ba_list)

# Range function

# 1.Initializing List using Range function:
list_r = list(range(1,10))
print(list_r)

# 2.Using Range in for loops:
# Q) print square of first 10 even numbers
for i in range(0,20,2):
    print(i**2)

# Sets    
# Sets are used to store multiple items in a single variable.Set cannot have duplicates.Sets can have mixed datatypes.
# 1)Remove duplicates form a list
list = [1,2,3,4,5,1,2,3123,21,312,3,2323,21,313,13,2,2,1,1,2,3,4,4]
newlist = set(list)
print(newlist)

# Initializing a new set
new_set = set()
# Adding and removing values from set
new_set.add('string')
new_set.add(2)
new_set.remove(2)
print(new_set)

# String Functions

string = 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Eaque, iste.'

print(string.capitalize()) # capitalizes first char
print(string.split('a')) #splits string for given value and returns list
print(string.title()) # capitalizes first char of every word
print(string.find('I')) # searches for give value in string and returns bool
print(string.index('n')) # Searches the string for a specified value and returns the position of where it was found
print(string[::-1]) # string concatenation