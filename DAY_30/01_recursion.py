#   Recursion in python

# Recursion is the process of defining something in terms
# of itself.

# A physical world example would be to place two parallel
# mirrors facing each other. Any object in between them
# would be reflected recursively.

# Python Recursive Function

# In Python, we know that a function can call other
# functions. It is even possible for the function to call
# itself. These types of construct are termed as recursive
# functions.                  

#FACTORIAL PROGRAM WITH THE HELP OF RECURSION
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(5))    

# 5! = 5 * fac(4)
#      5 * 4 * fac(3)
#      5 * 4 * 3 * fac(2)
#      5 * 4 * 3 * 2 * fac(1)
#      5 * 4 * 3 * 2 * 1



#PRINT FIBONACCI SERIES WITH THE HELP OF RESURSION
# Fibonacci series = 0,1,1,2,3,5,8,13,21.......
# f0 = 0 
# f1 = 1
# f2 = f0 + f1
# f3 = f2 + f1
# fn = fn-1 + fn-2
n = int(input("Enter a number: "))
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

for i in range(n):
    print(fibonacci(i))    
