#  There are several more in-built methods of the sets
# Set Methods

# There are several in-built methods used for the manipulation of
# set.They are explained below

# isdisjoint():

# The isdisjoint() method checks if items of given set are present in
# another set. This method returns False if items are present, else it
# returns True.

# Example:

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# print(cities.isdisjoint(cities2))

# Output:

# False

odd = {1,3,5,7,9,11}
even = {2,4,6,8,10}
print(odd.isdisjoint(even))


# issuperset():

# The issuperset() method checks if all the items of a particular set
# are present in the original set. It returns True if all the items are
# present, else it returns False.

# Example:

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Seoul", "Kabul"}
# print(cities.issuperset(cities2))
# cities3 = {"Seoul", "Madrid","Kabul"}
# print(cities.issuperset(cities3))

# Output:

# False
# False

print('\n')
asia = {'ind','pak','russia','shrilanka','china','nepal','thiland'}
country = {'ind','pak','china'}
print(asia.issuperset(country))
print(country.issubset(asia))

print('\n')
x = {1,243,4,5,7,8,6,4}
y = {2,4,7,6,234}
print(x.issuperset(y))


# add()

# If you want to add a single item to the set use the add() method.

# Example:

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.add("Helsinki")
# print(cities)

# Output:

# {'Tokyo', 'Helsinki', 'Madrid', 'Berlin', 'Delhi'}

print('\n')
name = {'rahul','riya','neha','aryan'}
name.add('chirag')
print(name)


# update()

# If you want to add more than one item, simply create another set or
# any other iterable object(list, tuple, dictionary), and use the
# update() method to add it into the existing set.

# Example:
print('\n')
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)

# Output:

# {'Seoul', 'Berlin', 'Delhi', 'Tokyo', 'Warsaw', 'Helsinki', 'Madrid'}


# remove() method is used to remove items from the set
print('\n')
ipl = {'RR','GT','SRH','RCB'}
ipl.remove('SRH')
print(ipl)

# The main difference between remove and discard is that, if we try
# to delete an item which is not present in set, then remove0 raises
# an error, whereas discard() does not raise any error.

print('\n')
ipl = {'RR','GT','SRH','RCB'}
ipl.discard('SRHE')
print(ipl)



# pop()

# This method removes the last item of the set but the catch is that
# we don't know which item gets popped as sets are unordered.
# However, you can access the popped item if you assign the pop0
# method to a variable.

# Example:
print('\n')
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

# Output:

# {'Tokyo', 'Delhi', 'Berlin'} 
# Madrid



# del

# del is not a method, rather it is a keyword which deletes the set
# entirely.

# Example:

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# del cities
# print(cities)

# Output:

# NameError: name 'cities' is not defined We get an error because our
# entire set has been deleted and there is no variable called cities
# which contains a set.

num = {1,3,5,6,3,57,3,0}
del num

# What if we don't want to delete the entire set, we just want to
# delete all items within that set?
# than we use clear()
# clear() method deletes all the items of set
num1 = {1,34,6,345,33,8,9,0,2}
num1.clear()
print(num1)



# Check if item is exist in the set or not
print('\n')
age = {20,11,12,14,15,17,18}
if 18 in age:
    print("age 18 is present in the set")
else:
    print("18 is not present")    

