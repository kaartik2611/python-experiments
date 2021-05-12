class Person:
    no_of_instances = 0                      # Counter variable

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.add_instance()                  # Counter will be incremented whenever a object is initiated

    @classmethod
    def add_instance(cls):                   # Increment the counter
        cls.no_of_instances +=1

    @classmethod
    def get_instance(cls):
        return cls.no_of_instances           # Static method to get value of counter

person1 = Person('Alvin', 19)
person2 = Person('Viren', 20)
person3 = Person('Shahid', 21)

# Add as much as instances as you want
print('Number of instances of Person class :', Person.get_instance())
