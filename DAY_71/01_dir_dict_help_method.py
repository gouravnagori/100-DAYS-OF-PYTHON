# The dir() method

# dir() : The dir0 function returns a list of all the attributes and
# methods (including dunder methods) available for an object. It is a
# useful tool for discovering what you can do with an object.
# Example:

print('\n')
name = ['ram','rahul','neha','riya']
print(dir(name))
print(name.__eq__)

print('\n')
tup = (2,3,5,212,'ok')
print(dir(tup))
print(tup.__sizeof__)


# __dict__: The  __dict__ attribute returns a dictionary  
# representation of an object's attributes. It is a useful tool for
# introspection. Example:
print('\n')
class Teacher:
    def __init__(self,name,dept):
        self.name = name
        self.dept = dept
        self.salary = 80000

t1 = Teacher('Davesh Bandil','CSE')        
print(t1.__dict__)

print('\n')
# help():
# the help() is use to get help documentation for an object,
# including a discription of its attributes and methods.
# print(help(int))
print(help(Teacher))