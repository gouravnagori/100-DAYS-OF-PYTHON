# Lambda Functions in Python

# In Python, a lambda function is a small anonymous function without a
# name. It is defined using the lambda keyword and has the following
# syntax:

# lambda arguments: expression

# Lambda functions are often used in situations where a small function
# is required for a short period of time. They are commonly used as
# arguments to higher-order functions, such as map, filter, and reduce.

# Here is an example of how to use a lambda function:

# # Function to double the input
# def double(x):
# return x * 2

# # Lambda function to double the input
# lambda x: x * 2

# The above lambda function has the same functionality as the double
# function defined earlier. However, the lambda function is anonymous,
# as it does not have a name.

# Lambda functions can have multiple arguments, just like regular
# functions. Here is an example of a lambda function with multiple
# arguments:



# def square(x):
#     return x**2
# same as
square = lambda x: x*2

print(square(3))

# we can take multiple values
avg = lambda x,y,z: (x+y+z)/3
print(avg(4,4,10))


cube = lambda x:x**3
print(cube(4))



def faltu(fn,x):
    return fn(x) + 20
                                            
print(faltu(lambda x: x**2 , 4))
 