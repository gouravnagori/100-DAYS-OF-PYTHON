# The time Module in Python

# The time module in Python provides a set of functions to work with time-
# related operations, such as timekeeping, formatting, and time
# conversions. This module is part of the Python Standard Library and is
# available in all Python installations, making it a convenient and essential
# tool for a wide range of applications. In this day 84 tutorial, we'll explore
# the time module in Python and see how it can be used in different
# scenarios.

# time.time()

# The time.time() function returns the current time as a floating-point
# number, representing the number of seconds since the epoch (the point
# in time when the time module was initialized). The returned value is
# based on the computer's system clock and is affected by time
# adjustments made by the operating system, such as daylight saving time.
# Here's an example:

# import time
# print(time.time())




import time

def using_while():
    i = 1
    while i<50001:
        i = i+1
        print(i)


def using_for():
    for i in range(1,50001):
        print(i)


# uncomment the loc 42,45,47 and 48 to see which loop is faster
init = time.time()
# using_while()
while_time = time.time() - init 
init = time.time()
# using_for()
for_time = time.time() - init 
# print(f"the time taken by for loop is {for_time}")
# print(f"the time taken by while loop is {while_time}")



print('\n')
print('hii')
# time.sleep(5)
print('I know i take 5 sec to print this')



t = time.localtime()
formate_time = time.strftime("%Y-%m-%d  %H:%M:%S",t)
print(formate_time)
