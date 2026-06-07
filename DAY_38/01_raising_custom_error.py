# Raising Custom errors

# In python, we can raise custom errors by using the
# raise keyword.

# salary = int(input("Enter salary amount: "))
# if not 2000 < salary < 5000:
#   raise ValueError("Not a valid salary")

# In the previous tutorial, we learned about different
# built-in exceptions in Python and why it is important to
# handle exceptions.However, sometimes we may need
# to create our own custom exceptions that serve our
# purpose.

# a = int(input("Enter a number between 5 and 10: "))
# if 5<a<10:
#     raise ValueError("Value should be between 5 and 10")

a = input("Enter a number between 5 and 9: ")
if a == 'quit':
    print("well")
elif int(a) < 5 or int(a) > 9:
    raise ValueError("The number should be 5 and 9")
