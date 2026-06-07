# List Comprehension

# List comprehensions are used for creating new lists from other iterables like lists,
# tuples, dictionaries, sets, and even in arrays and strings.

# Syntax:

# List = [Expression(item) for item in iterable if Condition]

# Expression: It is the item which is being iterated.

# Iterable: It can be list, tuples, dictionaries, sets, and even in arrays and strings.

# Condition: Condition checks if the item should be added to the new list or not.

# Example 1: Accepts items with the small letter "o" in the new list

# names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
# namesWith_0 = [item for item in names if "o" in item]
# print(namesWith_0)
# Output:

# ['Milo', 'Bruno', 'Rosa']

# Example 2: Accepts items which have more than 4 letters

# names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
# namesWith_0 = [item for item in names if (len(item) > 4)]
# print(namesWith_0)

# Output:

# ['Sarah', 'Bruno', 'Anastasia']

lst = [i for i in range(5)]
print(lst)


lst = [i*i for i in range(10+1) if i%2==0]
print(lst)

