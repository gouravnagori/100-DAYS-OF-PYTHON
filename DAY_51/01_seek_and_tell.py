# seek() and tell() functions

# In Python, the seek() and tell() functions are used to work with file
# objects and their positions within a file. These functions are part of
# the built-in io module, which provides a consistent interface for
# reading and writing to various file-like objects, such as files, pipes,
# and in-memory buffers.


# seek() function

# The seek0 function allows you to move the current position
# within a file to a specific point. The position is specified in
# bytes, and you can move either forward or backward from
# the current position. For example:

# with open('file.txt', 'r') as f:
# # Move to the 10th byte in the file
# f.seek(10)

# # Read the next 5 bytes
# data = f.read(5)    

# tell() function

# The tell() function returns the current position within the
# file, in bytes. This can be useful for keeping track of your
# location within the file or for seeking to a specific position
# relative to the current position. For example:

# with open('file.txt', 'r') as f:
# # Read the first 10 bytes
# data = f.read(10)

# # Save the current position
# current_position = f.tell()

# # Seek to the saved position
# f.seek(current_position)



with open("DAY_51/02_example.txt",'r') as f:
    f.seek(5)
    data = f.read(9)    
    print(data)     


print('\n')
with open("DAY_51/03_example.txt",'r') as f:
    f.seek(19)
    print(f.tell())
    data = f.read(200)    
    print(data)     

  
  