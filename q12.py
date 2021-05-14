import random
import threading

# dictionary which stores seat nos and names of people who got it
tickets = {
    'T01': '',
    'T02': '',
    'T03': '',
    'T04': '',
}

# Seats remaining to be alloted
remaining_seats = list(tickets)

# Function to randomly assign seats to people
def assign_ticket(dict, person, lock):
    lock.acquire()
    temp = random.choice(remaining_seats)
    dict[temp] = person.name
    remaining_seats.remove(temp)
    lock.release()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

lock = threading.Lock()

p1 = Person('Alvin', 19)
p2 = Person('Viren', 20)
p3 = Person('Payal', 19)
p4 = Person('Rahul', 19)

# Threads to simulate multiple people booking simultaneously
t1 = threading.Thread(target=assign_ticket, args=(tickets, p1, lock))
t2 = threading.Thread(target=assign_ticket, args=(tickets, p2, lock))
t3 = threading.Thread(target=assign_ticket, args=(tickets, p3, lock))
t4 = threading.Thread(target=assign_ticket, args=(tickets, p4, lock))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

# Display the assigned seats
for i in list(tickets):
    print(i, ':', tickets[i])    
