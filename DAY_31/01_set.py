# Python Sets

# Sets are unordered collection of data items. They
# store multiple items in a single variable. Set items are
# separated by commas and enclosed within curly
# brackets {}. Sets are unchangeable, meaning you
# cannot change items of the set once created. Sets do
# not contain duplicate items.

# Example:

# info = {"Carla", 19, False, 5.9, 19}
# print(info)

# Output:

# {False, 19, 5.9, 'Carla'}

# Here we see that the items of set occur in random
# order and hence they cannot be accessed using index
# numbers. Also sets do not allow duplicate values.

# Quick Quiz: Try to create an empty set. Check using
# the type0 function whether the type of your variable
# is a set


x = {1,2,6,6,3,5,"hari",1}
print(x)
print(type(x))

# In output we see that the items of set occur in random
# order and hence they cannot be accessed using index
# numbers. Also sets do not allow duplicate values.


# Quick Quiz: Try to create an empty set. Check using
# the type() function whether the type of your variable
# is a set

# empty_set = {} this is the empty dic
print('\n')
empty_set = set()
print(type(empty_set))


# Accessing set items:

# Using a For loop

# You can access items of set using a for loop.

# Example:

# info = {"Carla", 19, False, 5.9}
# for item in info:
# print(item)

# Output:

# False
# Carla
# 19
# 5.9

print("\n")
info = {'hii',23,51,'hello',23,True,None}
for i in info:
    print(i)