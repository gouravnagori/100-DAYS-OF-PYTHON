# Pyrthon provides several ways to manipulate files.
# here we discuss how to handle files in python

# Opening a File

# Before we can perform any operations on a file, we must first open it. Python
# provides the open( function to open a file. It takes two arguments: the name of
# the file and the mode in which the file should be opened. The mode can be 'r' for
# reading, 'w' for writing, or 'a' for appending.

# Here's an example of how to open a file for reading:

# f = open('myfile.txt', 'r')

# By default, the open() function returns a file object that can be used to read from
# or write to the file, depending on the mode.


# f = open("DAY_02/Nothing.txt",'r')
# text = f.read()
# print(text)
# f.close()


# Modes in file

# There are various modes in which we can open files.

# 1. read (r): This mode opens the file for reading only
# and gives an error if the file does not exist. This is the
# default mode if no mode is passed as a parameter.

# 2. write (w): This mode opens the file for writing only
# and creates a new file if the file does not exist.

# 3. append (a): This mode opens the file for appending
# only and creates a new file if the file does not exist.

# 4. create (x): This mode creates a file and gives an error
# if the file already exists.

# 5. text (t): Apart from these modes we also need to
# specify how the file must be handled. t mode is used
# to handle text files. t refers to the text mode. There is
# no difference between r and rt or w and wt since text
# mode is the default. The default mode is 'r' (open for
# reading text, synonym of 'rt'). 

# 6. binary (b): used to handle binary files (images, pdfs,
# etc).


# f = open("DAY_49/02_example.txt",'rb')
# text = f.read()
# print(text)
# f.close()


# Reading files
f = open("DAY_49/02_example.txt",'r')
text = f.read()
print(text)
f.close()

# Writing a files
# f = open("DAY_49/02_example.txt",'w')
# f.write("Hello, now your music will be deleted")
# f.close()

# Append mode 
f = open("DAY_49/02_example.txt",'a')
f.write("\nnow i have to write music once again")
f.close()

# via this logic we do not have to use close()
with open("DAY_49/02_example.txt",'a') as f:
    f.write("\nlife goes on in on in on in on in ")
