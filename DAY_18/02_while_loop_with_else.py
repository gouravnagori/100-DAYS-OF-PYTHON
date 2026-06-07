# Else with While Loop

# We can even use the else statement with
# the while loop. Essentially what the else
# statement does is that as soon as the
# while loop condition becomes False, the
# interpreter comes out of the while loop
# and the else statement is executed.

# Example:

x = 5
while(x > 0):
    print(x)
    x = x - 1
else:
    print('counter is 0')



# Do-while loop is not exist in python



# How to emulate do while loop in python?

# To create a do while loop in Python, you need to modify the while loop a
# bit in order to get similar behavior to a do while loop.

# The most common technique to emulate a do-while loop in Python is to
# use an infinite while loop with a break statement wrapped in an if
# statement that checks a given condition and breaks the iteration if that
# condition becomes true:

# Example

while True:
    number = int(input("Enter a positive number: "))
    print (number)
    if not number > 0:
        break

# Output

# Enter a positive number: 1
# 1
# Enter a positive number: 4
# 4
# Enter a positive number: -1
# -1

# Explanation

# This loop uses True as its formal condition. This trick turns the loop into
# an infinite loop. Before the conditional statement, the loop runs all the
# required processing and updates the breaking condition. If this condition
# evaluates to true, then the break statement breaks out of the loop, and
# the program execution continues its normal path.