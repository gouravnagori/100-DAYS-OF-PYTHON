# Inheritance in python

# When a class derives from another class. The child class will inherit all the public and
# protected properties and methods from the parent class. In addition, it can have its own
# properties and methods,this is called as inheritance.

# Python Inheritance Syntax

# class BaseClass:
#   Body of base class
# class DerivedClass(BaseClass):
#   Body of derived class

# Derived class inherits features from the base class where new features can be added to it.
# This results in re-usability of code.

# Types of inheritance:

# 1. Single inheritance
# 2. Multiple Inheritance
# 3. Multilevel inheritance
# 4. Hierarchical Inheritance
# 5. Hybrid Inheritance

# we will see explantion and example of each type of inhertance in few days


class Employee:
    def __init__ (self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee: {self. id} is {self.name}")

class Programmer(Employee):
    def showLanguage(self):
        print("The default langauge is Python")

e1 = Employee("Rohan Das", 400)
e1.showDetails()
e2 = Programmer("Harry", 4100)
e2.showDetails()
e2.showLanguage()



print('\n')
class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(f'{self.name} is {self.age} year old.')

class Dog(Animal):
    def __init__(self,name,age,skill):
        super().__init__(name,age)
        self.skill = skill
    def show1(self):    
        print(f'{self.name} has {self.skill} skill.')

d1 = Dog('Tommy',3,'Sprinting')
d1.show()
d1.show1()      


print('\n')
class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(f'{self.name} is {self.age} year old.')

class Dog(Animal):
    def show1(self):    
        print(f'{self.name} has Barking skill.')

d1 = Dog('Tommy',3)
d1.show()
d1.show1()  