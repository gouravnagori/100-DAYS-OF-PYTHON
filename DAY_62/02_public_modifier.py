# Public Access Specifier in Python

# All the variables and methods (member functions) in python are by default
# public. Any instance variable in a class followed by the 'self' keyword ie.
# self.var_name are public accessed.

# Example:

class Student:
# constructor is defined
    def __init__(self, age, name):
        self.age = age
        self.name = name

obj = Student(21,"Harry")
print(obj.age)
print(obj.name)
print(dir(obj))
# public variable
# public variable

# Output:

# 21
# Harry


