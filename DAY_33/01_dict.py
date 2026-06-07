# Python Dictionaries

# Dictionaries are ordered collection of data items. They store multiple items in a single
# variable. Dictionary items are key-value pairs that are separated by commas and
# enclosed within curly brackets {}.

# Example:

# info = {'name': 'Karan', 'age':19, 'eligible':True}
# print( info)

# Output:

# {'name' : 'Karan', 'age': 19, 'eligible': True} 



# Accessing Dictionary items:

# I. Accessing single values:

# Values in a dictionary can be accessed using
# keys. We can access dictionary values by
# mentioning keys either in square brackets or by
# using get method.

# Example:

# info = {'name' : 'Karan', 'age' : 19,
# 'eligible':True}
# print( info['name' ])
# print(info.get('eligible'))

# Output:

# Karan
# True


dict = {'name' : 'gourav',
        'age' : 19,
        'eligible' : True}
print(dict)
print(dict['name'])
print(dict.get('name'))


emp_id = {
    11: 'a', 12:'c' , 13:'f'
}
print(emp_id)
print(emp_id[13])


print('\n')

# II. Accessing multiple values:

# We can print all the values in the dictionary using
# values( method.

# Example:

# info = {'name': 'Karan', 'age':19,
# 'eligible':True}
# print(info.values())

#  Output:

# dict_values(['Karan', 19, True])

info = {
    'name':'a','age':12,'hight':6
}
print(info.keys())
print(info.values())

for key in info.keys():
    print(f"the value corresponding to the key {key} is {info[key]}")


print(info.items())
for key,value in info.items():
     print(f"the value corresponding to the key {key} is {info[key]}")
