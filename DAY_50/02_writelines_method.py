# writelines() method

# The writelines0 method in Python writes a sequence of strings to a
# file. The sequence can be any iterable object, such as a list or a
# tuple.

# Here's an example of how to use the writelines0 method:

# f = open('myfile.txt', 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()

# This will write the strings in the lines list to the file myfile.txt. The
# n characters are used to add newline characters to the end of
# each string.

# Keep in mind that the writelines0 method does not add newline
# characters between the strings in the sequence. If you want to add
# newlines between the strings, you can use a loop to write each
# string separately:

# f = open('myfile.txt', 'w')
# lines = ['line 1', 'line 2', 'line 3']
# for line in lines:
#   f.write(line + '\n')
# f.close()

# this is also good method to close the file
# after you are done with it
