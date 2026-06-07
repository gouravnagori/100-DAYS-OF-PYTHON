# Enumerate function in python

# The enumerate function is a built-in function in Python that allows
# you to loop over a sequence (such as a list, tuple, or string) and get
# the index and value of each element in the sequence at the same
# time. Here's a basic example of how it works:

# # Loop over a list and print the index and value of
# each element
# fruits = ['apple', 'banana', 'mango' ]
# for index, fruit in enumerate(fruits):
#   print(index, fruit)

# The output of this code will be:

# apple
# 1 banana
# 2 mango

# As you can see, the enumerate function returns a tuple containing the
# index and value of each element in the sequence. You can use the for
# loop to unpack these tuples and assign them to variables, as shown
# in the example above.


marks = [12,42,45,24,34,65,74]

# index = 0
# for mark in marks:
#     print(mark)
#     if index == len(marks) - 2:
#         print("oh you got 65 marks")
#     index += 1    

for index,mark in enumerate(marks):
    print(f"{mark} with the {index}")
    if index == len(marks) - 2:
        print("oh you got 65 marks")
    

# Changing the start index

# By default, the enumerate function starts the index at 0, but you can
# specify a different starting index by passing it as an argument to the
# enumerate function:

# # Loop over a list and print the index (starting at 1)
# and value of each element
print('\n')
fruits = ['apple', 'banana', 'mango' ]
for index, fruit in enumerate(fruits, start=1):
  print(index, fruit)

# This will output:

# 1 apple
# 2 banana
# 3 mango

# The enumerate function is often used when you need to loop over a
# sequence and perform some action with both the index and value of
# each element. For example, you might use it to loop over a list of
# strings and print the index and value of each string in a formatted
# way:

# fruits = ['apple', 'banana', 'mango' ]
# for index, fruit in enumerate(fruits):
#   print(f'{index+1}: {fruit}')

# This will output:

# 1: apple
# 2: banana
# 3: mango

print('\n')
animal = ['cow','dog','loin','tiger']
for index,animal in enumerate(animal,start = 1):
   print(f"{index}. {animal}.")
   