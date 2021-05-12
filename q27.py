global_var = 'Global Variable'                 # This is a global variable

def print_global():                            # This function prints the global variable we defined in line 1
    print(global_var)

def print_local():
    local_var = 'Local Variable'               # This is local variable which is only accessible inside this block/scope
    print(local_var)

def modify_global():
    global global_var                          # To change the value of the
    global_var = 'New global variable'         # actual global variable in line 1
    print(global_var)

print_global()
print_local()
modify_global()
print_global()                                 # Print the global variable again to show we actually modified it
