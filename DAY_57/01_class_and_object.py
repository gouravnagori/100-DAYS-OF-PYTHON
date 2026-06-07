# Creating a Class:

# Let us now create a class using the class keyword.

# class Details:
#   name = "Rohan"
#   age = 20

# Creating an Object:

# Object is the instance of the class used to access the properties of the class
# Now lets create an object of the class.

# Example:

# obj1 = Details()

# Now we can print values:

# Example:    

# class Details:
# name = "Rohan"
# age = 20

# obj1 = Details()
# print(obj1.name)
# print(obj1.age)

# Output:

# Rohan
# 20

class Info:
    name = 'harish'
    dob = '2 nov 2001'
    def brief(self):
        print(f'{self.name} is born on {self.dob}')

a = Info()
a.name = 'hariom'
print('\n',a.name,'\n',a.dob,'\n') 
a.brief()       