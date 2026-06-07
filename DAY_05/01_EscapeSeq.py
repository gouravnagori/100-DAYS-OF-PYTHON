# Escape-sequence character
# To insert characters that cannot be directly used in a string, we use an escape sequence character.

# An escape sequence character is a backslash \ followed by the character you want to insert.

# An example of a character that cannot be directly used in a string is a double quote inside a string that is surrounded by double quotes

# print("This doesnt "execute")
# print("This will \ execute")

print("hello who are you?\nAnd where are you living?")

print("\noh you are \"Gourav\"\nAnd you are from Jaipur.")

print('Hyy who are \'you')

print("how","the","jos",100,"sir")
print("how","the","jos",100,"sir",sep="~")
print("how","the","jos",100,"sir",sep="!")
print("how","the","jos",100,"sir",sep="~",end="Ok")



# Other Parameters of Print Statement

# 1. object(s): Any object, and as many as you like. Will be converted to
# string before printed
# 2. sep='separator': Specify how to separate the objects, if there is more
# than one. Default is "
# 3. end='end': Specify what to print at the end. Default is 'In' (line feed)
# 4. file: An object with a write method. Default is sys.stdout

# Parameters 2 to 4 are optional
