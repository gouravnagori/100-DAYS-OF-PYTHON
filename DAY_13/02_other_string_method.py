# isalnum():

# The isalnum() method returns True only if the entire string only consists
# of A-Z, a-z, 0-9. If any other characters or punctuations are present, then
# it returns False.

# Example 1:

# str1 = "WelcomeToTheConsole"
# print(str1.isalnum())

# Output:

# True

str = "Welcome to the Wrestelminia Season 9"
print(str.isalnum()) #it return False because there are whitespaces

str = "WelcometotheWrestelminiaSeason9"
print(str.isalnum()) #True




# isalpha():

# The isalpha() method returns True only if the entire string only consists
# of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are
# present, then it returns False.

# Example :

str1 = "Welcome"
print(str1.isalpha())  #True                

str2 = "itismatchnumber10"
print(str2.isalpha())  #False



# islower() :

# The islower() method returns True if all the characters in the string are
# lower case, else it returns False.

# Example:
# str1 = "hello world"
# print(str1.islower())

# Output:
# True
str1 = "hello world"
print(str1.islower()) #True

str2 = "     "
print(str2.islower()) #False

str3 = "i think they call this love.54"
print(str3.islower()) #True

str4 = "I think they call this love.54"
print(str4.islower()) #False




# isprintable|() :

# The isprintable() method returns True if all the values within the given
# string are printable, if not, then return False.

# Example :

# str1 = "We wish you a Merry Christmas"
# print(str1.isprintable())

# Output:
# True
print('\n')
str1 = "We wish you a Merry Christmas"
print(str1.isprintable())

str1 = "We wish\n you a Merry\t Christmas"
print(str1.isprintable())



# isspace() :

# The isspace() method returns True only and only if the string contains
# white spaces, else returns False.

# Example:

# str1 = "       "
# print(str1.isspace())
# str2 ="          "
# print(str2.isspace())

# #using Spacebar

# #using Tab

# Output:

# True
# True    
str = "sfjhgsdf      isdufuy     dfsyd f   "
print(str.isspace()) #False




# istitle() :

# The istitile() returns True only if the first letter of each word of the
# string is capitalized, else it returns False.

# Example:

str1 = "World Health Organization"
print(str1.istitle()) #True

str2 = "To kill a Mocking bird"
print(str2.istitle()) #False



# swapcase() :

# The swapcase() method changes the character casing of the string. Upper
# case are converted to lower case and lower case to upper case.

# Example:

# str1 = "Python is a Interpreted Language"
# print(str1.swapcase())

# Output:

# pYTHON IS A iNTERPRETED LANGUAGE

str = "Today is the BeautTful Day"
print(str.swapcase())




# title():

# The title() method capitalizes each letter of the word within the string.

# Example:

str1 = "He's name is dan. dan is an honest man."
print(str1.title())

# Output:

# He'S Name Is Dan. Dan Is An Honest Man.