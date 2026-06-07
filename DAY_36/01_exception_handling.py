# Exception Handling

# Exception handling is the process of responding to unwanted or unexpected
# events when a computer program runs. Exception handling deals with these
# events to avoid the program or system crashing, and without this process,
# exceptions would disrupt the normal operation of a program.

# Exceptions in Python

# Python has many built-in exceptions that are raised when your program
# encounters an error (something in the program goes wrong).

# When these exceptions occur, the Python interpreter stops the current process
# and passes it to the calling process until it is handled. If not handled, the program
# will crash.

num = (input("Enter a number: "))
print(f"the multiplication table of {num} is: ")
try:
    for i in range(1,11):
        print(f"{int(num)}x{i} = {int(num)*i}")
except Exception as e:
    print(e)

print('some important line of code')
print('end of the progeam')    


print('\n')
num = (input("Enter a number: "))
print(f"the multiplication table of {num} is: ")
try:
    for i in range(1,11):
        print(f"{int(num)}x{i} = {int(num)*i}")
except:
    print('Invalid input by the user')

print('some important line of code')
print('end of the progeam')    



print('\n')

try:
    num = int((input("Enter a number: ")))
    print(f"the multiplication table of {num} is: ")
    for i in range(1,11):
        print(f"{num}x{i} = {num*i}")
except:
    print('Invalid input by the user')

print('some important line of code')
print('end of the progeam')   



print('\n')
try:
    num = int(input("Enter an integer number: "))
    print("Valid input")
    list = [2,15,874,3]
    print(list[num])
except ValueError:
    print('Enter number is not integer')

except IndexError:
    print('Invalid index')       

