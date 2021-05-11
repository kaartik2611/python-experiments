import pickle

object = {
    'Python' : ['Django','Flask','Numpy'],
    'JavaScript' : ['React','Vue','Angular'],
    'Java' : ['JavaFX','Oracle','Spring']
}

# pickling
filename = "pickle.txt"
file = open(filename,'wb')
pickle.dump(object,file)
file.close()

# unpickling
file = open(filename,'rb')
unpickle = pickle.load(file)

print(unpickle['Python'])

