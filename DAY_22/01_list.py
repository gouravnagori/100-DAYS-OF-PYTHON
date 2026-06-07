# Python Lists

# · Lists are ordered collection of data items.
# . They store multiple items in a single variable.
# . List items are separated by commas and enclosed within square
# brackets [].
# . Lists are changeable meaning we can alter them after creation.

# Example 1:

# lst1 = [1,2,2,3,5,4,6]
# lst2 = ["Red", "Green", "Blue"]
# print(lst1)
# print(lst2)

# Output:

# [1, 2, 2, 3, 5, 4,6]
# ['Red', 'Green', 'Blue']



hight = [233,123,457,7,73,1123,123,456,8786,'idk',False]
print(type(hight))
print(hight)
for i in range(len(hight)):
    print(hight[i])
print(hight)

hight[8] = 237
print(hight)

if 'idk' and 233 in hight:
    print("Yes")
else:
    print("No")    


print("\n")
marks = [43,57,33,86,89,53]
print(marks[-4])  #Negative indexing
print(marks[len(marks)-4])  #Positive indexing
print(marks[6-4])  #Positive indexing
print(marks[2])  #Positive indexing



# Check whether an item in present in the list?

# We can check if a given item is present in the list. This is done using the
# in keyword.

# colors = ["Red", "Green", "Blue", "Yellow", "Green"]
# if "Yellow" in colors:
#   print("Yellow is present.")
# else:
#   print("Yellow is absent.")

# Output:

# Yellow is present.
print("\n")
name = ['gourav','chirag','koushal','rahul']
if 'mahesh' in name:
    print("Yes mahesh is present in the list")
else:
    print("mahesh is Not present in the list")    


#Same thing apply for string as well
if "Ram" in "JayShreeRam":
    print("Yes")
else:
    print("No")    

