import random
import threading

# Dictionary which stores berths and names of people who got it
berths = {
    1 : '',
    2 : '',
}

# Seats remaining to be alloted
remaining_berths = list(berths)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Function to randomly allot berths to people
def allot_berth(dict, person, lock):
    lock.acquire()
    temp = random.choice(remaining_berths)
    dict[temp]=person.name
    remaining_berths.remove(temp)
    lock.release()

lock = threading.Lock()

p1 = Person('Alvin', 19)
p2 = Person('Viren', 20)

t1 = threading.Thread(target=allot_berth, args=(berths, p1, lock))
t2 = threading.Thread(target=allot_berth, args=(berths, p2, lock))

t1.start()
t2.start()

t1.join()
t2.join()

# Display the assigned berths
for i in list(berths):
    print(i, ':', berths[i])    
