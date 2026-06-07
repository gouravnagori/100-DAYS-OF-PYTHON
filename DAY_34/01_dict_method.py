# update()
marks = {
    'ram' : 12,
    'shyam' : 64,
    'rahul': 89
}
    
marks2 = {
    'chirag' : 92,
    'govind' : 94,
    'sahil': 89
}

marks.update(marks2)
print(marks)
marks.update({'koushal':99,'dilip':100})
print(marks)
print('\n')


#clear()
color = {
    'page' : 'white',
    'pc'   : 'black',
    'sky'  : 'blue'
}
print(color)
color.clear()
print(color)
print('\n')


# Empty dict
empty = {}
print(empty)
print('\n')



# pop() -> use to removes key-value pairs whose key is passed as a parameter
color = {
    'page' : 'white',
    'pc'   : 'black',
    'sky'  : 'blue'
}
color.pop('pc')
print(color)
print('\n')


# popitem() -> use to remove last key value pair from the dictonary
color = {
    'page' : 'white',
    'pc'   : 'black',
    'sky'  : 'blue',
    'sun'  : 'white',
    'marse': 'red'
}
color.popitem()
print(color)
print('\n')


# del:

# we can also use the del keyword to remove a dictionary item.

# Example:

info = {'name': 'Karan', 'age':19, 'eligible':True,
'DOB' : 2003}
del info['eligible']
print(info)

# Output:

{'name': 'Karan', 'eligible': True, 'DOB': 2003}

# If key is not provided, then the del keyword will delete the dictionary
# entirely.

# Example:

info = {'name': 'Karan', 'age':19, 'eligible':True,
'DOB':2003}
del info
print( info)

# Output:

# NameError: name 'info' is not defined

