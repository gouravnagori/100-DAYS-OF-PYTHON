# Manipulating Tuples

# Tuples are immutable, hence if you want to add, remove or change tuple
# items, then first you must convert the tuple to a list. Then perform operation
# on that list and convert it back to tuple.

# Example:

# countries = ("Spain", "Italy", "India", "England", "Germany")
# temp = list(countries)
# temp. append( "Russia")
# temp.pop(3)
# temp[2] = "Finland"
# countries = tuple(temp)
# print(countries)

# Output:

# ('Spain', 'Italy', 'Finland', 'Germany', 'Russia')

# Thus, we convert the tuple to a list, manipulate items of the list using list
# methods, then convert list back to a tuple.

# #add item
# #remove item
# #change item


countries = ('india','russia','china','italy')
temp = list(countries)
temp.append('usa')
temp.pop(2)
temp[2] = 'finland'
countries = tuple(temp)
print(countries)

#However we can directly concatenate two tuples without converting them to list.
even = (2,4,6,8,10)
odd = (1,3,5,7,9)
mixed = even + odd
print(mixed)


#                           `METHODS`
# Tuple methods

# As tuple is immutable type of collection of elements it have limited
# built in methods.They are explained below

# count() Method

# The count() method of Tuple returns the number of times the given
# element appears in the tuple.

# Syntax:

# tuple.count(element)

# Example

# Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
# res = Tuple1.count(3)
# print('Count of 3 in Tuple1 is:', res)

# Output
# 3

tup1 = ('hii','hello','hii','ok','hii','namaste')
print(tup1)
print("lenght of the tup1 is",len(tup1))
print(tup1.count('hii'))
print(tup1.index('hello')) #print the index no. of the first occurence of 'hello'
print(tup1.index('hii',1,4)) #now it show the index no. of hii in the first occurence in indexes 1 to 4 
# print(tup1.index('salam')) #it shows ValueError because this is not present in the string

