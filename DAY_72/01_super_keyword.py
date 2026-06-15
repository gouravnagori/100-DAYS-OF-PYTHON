# Super keyword in Python

# The super() keyword in Python is used to
# refer to the parent class. It is especially
# useful when a class inherits from multiple
# parent classes and you want to call a
# method from one of the parent classes.

# When a class inherits from a parent class,
# it can override or extend the methods
# defined in the parent class. However,
# sometimes you might want to use the
# parent class method in the child class.
# This is where the super0 keyword comes
# in handy.

# Here's an example of how to use the
# super0 keyword in a simple inheritance
# scenario:


class Parent:
    def parent_call(self):
        print('Calling parent class.')
class Child(Parent):
    def parent_call(self):
        print("Achha ji esa h kya")
        super().parent_call()
    def child_call(slef):
        print("calling child class.")
        super().parent_call()

c1 = Child()
c1.child_call()      
c1.parent_call()


print('\n')
class Teacher:
    def __init__(self,name,id):
        self.name = name
        self.id  = id

class Teacher_hidden_info(Teacher):
    def __init__(self, name, id , salary):
        super().__init__(name, id)
        self.salary = salary

t1 = Teacher_hidden_info('Er Ram Babu Buri',236,90333)
print(t1.id)
print(t1.salary)            
