print("Append method")
l = [1,3,12,5,10,7,34,5]
print(l)
l.append(2)
print(l) 

print("sort method")
l.sort()
print(l)
l.sort(reverse=True)
print(l)

print("reverse method")
l1=[21,34,2,4,74,1,90]
l1.reverse()
print(l1)

l2=[2,2,4,21,46,754,2,10]
print(l2)
print(l2.index(46))  #this method returns the index of the occurence of the list items
print(l2.count(2))


# copy()

# Returns copy of the list. This can be done to perform operations on the
# list without modifying the original list.

# Example:

# colors = ["voilet", "green", "indigo", "blue"]
# newlist = colors.copy()
# print(colors)
# print(newlist)

# Output:

# ['voilet', 'green', 'indigo', 'blue']
# ['voilet', 'green', 'indigo', 'blue']

print("\n")
l3 = [23,21,3,6,74,3,2,5,6]
print(l3)
copy_list = l3.copy()
print(copy_list)
copy_list[0] = 10
print(copy_list)
print(l3)
#Because lists are immutable


l4=[2,1,2,34,3,26,3,6,6]
l4.insert(2,69)
print(l4)


print("\n")
# extend():

# This method adds an entire list or any other collection datatype (set,
# tuple, dictionary) to the existing list.

# Example 1:

# #add a list to a list
# colors = ["voilet", "indigo", "blue"]
# rainbow = ["green", "yellow", "orange", "red"]
# colors.extend(rainbow)
# print(colors)

# Output:

# ['voilet', 'indigo', 'blue', 'green', 'yellow', 'orange','red']
x = [1,2,36,34,3,70]
y = [122,311,432,754]
x.extend(y)
print(x)
y.extend(x)
print(y)

#concatinating of list
print('\n')
u = [1,3,3,4,3,'hii']
v = ['ok',423,45,3,'well']
w = u+v
print(w)