# truncate() function

# When you open a file in Python using the open function, you
# can specify the mode in which you want to open the file. If
# you specify the mode as 'w' or 'a', the file is opened in write
# mode and you can write to the file. However, if you want to
# truncate the file to a specific size, you can use the truncate
# function.

# Here is an example of how to use the truncate function:

# with open('sample.txt', 'w') as f:
# f.write( 'Hello World!')
# f.truncate(5)

# with open('sample.txt', 'r') as f:
# print(f.read())


with open("DAY_51/05_example.txt",'w') as f:
    f.write('this is the beautiful day')
    f.truncate(10)

f = open("DAY_51/05_example.txt",'r')
data = f.read()
print(data)
f.close()