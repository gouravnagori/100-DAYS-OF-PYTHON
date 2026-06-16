# Multiple inheritance is a powerful feature in oop 
# that allows a class the inherit the attributes and methid from 
# multiple parent classes. this can be useful in situation where a class
# need to inherit functionality from multiple source.

class Manager:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(f'The name of the manager is {self.name}')
class Employee:
    def __init__(self,position):
        self.position = position
    def show(self):
        print(f'The position is {self.position}')
class Manager_Employee(Manager,Employee):
    def __init__(self, name, position):
        self.name = name
        self.position = position

m_e = Manager_Employee('Rahul','HR')
print(m_e.name)        
print(m_e.position)    
m_e.show()
print(Manager_Employee.mro())    

# It's important to note that, in case of multiple inheritance, 
# Python follows a method resolution order (MRO) to resolve conflicts between methods or attributes from different
# parent classes. The MRO determines the order in which parent classes are searched for attributes and methods.


print('\n')
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")
        
class Mammal:
    def __init__(self, name, fur_color):
        self.name = name
        self.fur_color = fur_color
        
class Dog(Animal, Mammal):
    def __init__(self, name, breed, fur_color):
        Animal.__init__(self, name, species="Dog")
        Mammal.__init__(self, name, fur_color)
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")
