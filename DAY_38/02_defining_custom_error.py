# Defining Custom Exceptions

# In Python, we can define custom exceptions by creating
# a new class that is derived from the built-in Exception
# class.

# Here's the syntax to define custom exceptions:

class CustomError(Exception):
    # code
    pass

    # try:
        # code

    # except CustomError:
        
        # code ...

# . ..

# This is useful because sometimes we might want to do
# something when a particular exception is raised. For
# example, sending an error report to the admin, calling
# an api, etc.