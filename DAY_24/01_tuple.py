# Python Tuples

# Tuples are ordered collection of data items. They store multiple items in a single
# variable. Tuple items are separated by commas and enclosed within round brackets ().
# Tuples are unchangeable meaning we can not alter them after creation.

# Example 1:

# tuple1 = (1,2,2,3,5,4,6)
# tuple2 = ("Red", "Green", "Blue")
# print(tuple1)
# print(tuple2)

# Output:

# (1, 2, 2, 3, 5, 4, 6)
# ('Red', 'Green', 'Blue')

tup = (1,2,False,24,324,"Rahul")
print(type(tup))
print(tup)
print(tup[0],tup[1],tup[2])
tup = (1,) #single element tuple
print(tup)


#Negative indexing is same as list and strings
print("\n")
tup2 = (3,56,875,2,5,6,7)
print(len(tup2))
print(tup2[-3])
print(tup2[len(tup2)-3])

print(tup2[:])
print(tup2[:4])
print(tup2[2:])
print(tup2[1:3])
print(tup2[-4:-1])
print(tup2[-1:-6]) # this o/p is ()
print(tup2[1:6]) 
print(tup2[1:6:2]) 


if 875 in tup2:
    print("Yes 875 is present in tup2")
else:
    ("875 is not present")    