# In python string is like an array of characters.
# we can access the part of the string by using index number which start with 0.
# square brackets is use to access the element of the string.

name = "veer pratap singh"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(len(name))
# print(name[17]) it throws an error


print("using for loop")
for character in name:
    print(character)


song = '''i saw i think your face today
but i justturn my head away...'''    
for character in song:
    print(character)