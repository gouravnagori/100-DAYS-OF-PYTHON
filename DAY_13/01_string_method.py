# Strings are immutable in python
# existing string can not be changed
name = "Rahul"
print("it converts entire string into upper case:",name.upper())
print("it converts entire string into lower case:",name.lower())
print("\n")



# rstrip() :
# the rstrip() removes any trailing characters. Example:
# str3 = "Hello !!! "
# print(str3.rstrip("!"))
str1 = "!!!omg!!!!"
print(str1)
print(str1.rstrip('!'))
str2 = "...ok....."
print(str2)
print(str2.rstrip('.'))
print("\n")


# replace()
# the replace() method replaces all the occurances of string with another string.
quote = "fishes jumps high, but only in water, so don't be like fishes"
print(quote)
print(quote.replace("fishes","sharks"))




# split()
# The split() method splits the given string at the specified instance and returns the separated
# strings as list items.

# Example:
# str2 = "Silver Spoon"
# print(str2.split(" "))

# #Splits the string at the whitespace
# Output:
# ['Silver', 'Spoon']
# There are various other string methods that we can use to modify our strings.

str3 = "Chirag is a chomu."
print(str3.split())




# capitalize() :

# The capitalize() method turns only the first character of the string to uppercase and the rest other
# characters of the string are turned to lowercase. The string has no effect if the first character is
# already uppercase.
# and it automatically turn other letters into lowercase

str4 = "i like YOur Party dREss. He say you sUCh a mess."
print(str4.capitalize())




# center() :

# The center() method aligns the string to the center as per the
# parameters given by the user.

# Example:

# str1 = "Welcome to the Console !!! "
# print(str1.center(50))

# Output:
#               Welcome to the Console !!!

# We can also provide padding character. It will fill the rest of
# the fill characters provided by the user.

# Example:
# str1 = "Welcome to the Console !!! "
# print(str1.center(50,"."))
# Output:

# ...............Welcome to the

# Console !!!..................

str5 = "Welcome to the NewYork City"
print(len(str5))
print(str5.center(60))
print(str5.center(60,"!"))




# count() :

# The count() method returns the number of times the given
# value has occurred within the given string.

# Example:

# str2 = "Abracadabra"
# countStr = str2.count("a")
# print(countStr)

# Output:
# 4   

str7 = "dhkdjksd adjkadh kajsdhakdakd kdhakdaksdha ksdh dhaaksdhkashd"
print(str7.count(' '))
print(str7.count('d'))
print(str7.count('dh'))
print(str7.count('xkdjfd'))




# endswith() :

# The endswith() method checks if the string ends with a given value. If
# yes then return True, else return False.

# Example :
# str1 = "Welcome to the Console !!! "
# print(str1.endswith(" !!! "))

# Output:
# True

# We can even also check for a value in-between the string by providing
# start and end index positions.
str8 = "May be RR will win this season"
print(str8.endswith("season"))
print(str8.endswith("hii"))
print(str8.endswith("RR",2,9))

#and vice versa with the startswith() 



# find():

# The find() method searches for the first occurrence of the given value
# and returns the index where it is present. If given value is absent from
# the string then return -1.

# Example:
# str1 = "He's name is Dan. He is an honest man."
# print(str1.find("is"))

# Output:
# 10

str9 = 'is there any chance to win 20000M $'
print("The first occurance of there is index number",str9.find('there'))
print(str9.find("58ghkg"))#it shows -1





# index() :

# The index() method searches for the first occurrence of the given value
# and returns the index where it is present. If given value is absent from
# the string then raise an exception.

# Example:

# str1 = "He's name is Dan. Dan is an honest man."
# print(str1.index("Dan"))

# Output:

# 13

# As we can see, this method is somewhat similar to the find0 method.
# The major difference being that index0 raises an exception if value is
# absent whereas find( does not.  


str9 = 'is there any chance to win 20000M $ and any chance to loss 20000M $'
print(str9.index("$"))
print(str9.index("Mrbeast")) #now it shows error not -1
