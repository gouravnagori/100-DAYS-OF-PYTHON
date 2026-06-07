x = 100
print(x)
def fun():
    x = 50
    print(f"the local variable is {x}")
    print("wowww")

print(f"the global variable is {x}")
fun()
x = 50
print(f"the global variable is {x}")




print('\n')
x = 10 # global variable

def my_function():
    global x
    x = 90
    y = 5 # local variable
    print(y)

my_function()
print(x)
# print(y) # this will cause an error because y is a local variable and is not
# accessible outside of the function
