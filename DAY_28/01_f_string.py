# String formatting in python

# String formatting can be done in python using the format method.

# txt = "For only {price :. 2f} dollars!"
# print(txt.format(price=49))

# f-strings in python

# It is a new string formatting mechanism introduced by the PEP 498. It
# is also known as Literal String Interpolation or more commonly as F-
# strings (f character preceding the string literal). The primary focus of
# this mechanism is to make the interpolation easier.

# When we prefix the string with the letter 'f', the string becomes the f-
# string itself. The f-string can be formatted in much same as the
# str.format0 method. The f-string offers a convenient way to embed
# Python expression inside string literals for formatting.


#           OLD METHOD
letter = 'my name is {} and i am from {}'
country = 'India'
name = 'Gourav'
print(letter.format(name,country))

letter = 'my name is {1} and i am from {0}'
country = 'India'
name = 'Gourav'
print(letter.format(name,country))


#           NEW METHOD
name1 = 'om'
sport = 'Cricket'
print(f"His name is {name1} ane he is playing{sport}")


price = 49.09423
print(f"The price of the apple is {price:.2f}")


print(f'{3*5}')
print(type(f'{3*5}'))


print(f"i want to show f-string like this: His name is {{name1}} ane he is playing {{sport}}")


