# Docstrings in python

# Python docstrings are the string literals that appear
# right after the definition of a function, method, class,
# or module.

# Example

# def square(n):
# '''Takes in a number n, returns the
# square of n'''
# print(n ** 2)
# square(5)

# Here,

# "'Takes in a number n, returns the square of n'" is a
# docstring which will not appear in output

# Output:

# 25

# Python doc attribute

# Whenever string literals are present just after the
# definition of a function, module, class or method,
# they are associated with the object as their doc
# attribute. We can later use this attribute to retrieve
# this docstring.

# Example

# def square(n):
# '''Takes in a number n, returns the
# square of n'''
# return n ** 2

# print(square .__ doc __ )

# Output:

# Takes in a number n, returns the square of n


def sum(a,b):
    ''' here we take two inputs and add them after that we shows the output'''
    print('sum is:',(a+b))
sum(3,5)    


def sum(a,b):
    ''' here we take two inputs and add them after that we shows the output'''
    print('sum is:',(a+b))
sum(3,5)    
print(sum.__doc__)


def sum(a,b):
    print("hii")
    ''' here we take two inputs and add them after that we shows the output'''
    print('sum is:',(a+b))
sum(3,5)    
print(sum.__doc__) #o/p is None because Doc string is just written after fun defination


# Python Comments vs Docstrings

# Python Comments

# Comments are descriptions that help programmers
# better understand the intent and functionality of the
# program. They are completely ignored by the Python
# interpreter.

# Python docstrings

# As mentioned above, Python docstrings are strings
# used right after the definition of a function, method,
# class, or module (like in Example 1). They are used to
# document our code.

# We can access these docstrings using the doc
# attribute.
