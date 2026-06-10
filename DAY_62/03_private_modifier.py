# Private Access Modifier

# By definition, Private members of a class (variables or methods) are those
# members which are only accessible inside the class. We cannot use
# private members outside of class.

# In Python, there is no strict concept of "private" access modifiers like in
# some other programming languages. However, a convention has been
# established to indicate that a variable or method should be considered
# private by prefixing its name with a double underscore (__). This is known
# as a "weak internal use indicator" and it is a convention only, not a strict
# rule. Code outside the class can still access these "private" variables and
# methods, but it is generally understood that they should not be accessed
# or modified.

# Example:

class Employee:
    def __init__(self):
        self.__name = "Hariom" #an indication on private variable

    def __funname(self):   #an indication on private function
        self.y = 3
        print(self.y)
e1 = Employee()
# print(e1.__name) #can not be access directly
# print(e1.__funname())  #can not be access directly

#  But can be access indirectly
print(e1._Employee__name) 
e1._Employee__funname()



# Name mangling

# Name mangling in Python is a technique used to protect class-private and
# superclass-private attributes from being accidentally overwritten by
# subclasses. Names of class-private and superclass-private attributes are
# transformed by the addition of a single leading underscore and a double
# leading underscore respectively.


class MyClass:
    def __init__(self):
        self.__private_attribute = "I am a private attribute"
        self.__mangled_attribute = "I am a mangled attribute"

my_object = MyClass()

print(my_object.__private_attribute) # Output: I am a private attribute
print(my_object.__mangled_attribute) # Throws an AttributeError
print(my_object._MyClass__mangled_attribute) # Output: I am a mangled attribute
print(my_object.__dir__())
# In the example above, the attribute _private_attribute is marked as
# private by convention, but can still be accessed from outside the class.
# The attribute __ mangled_attribute is private and its name is "mangled" to
# _MyClass __ mangled_attribute, so it can't be accessed directly from
# outside the class, but you can access it by calling
# _MyClass __ mangled_attribute
 

