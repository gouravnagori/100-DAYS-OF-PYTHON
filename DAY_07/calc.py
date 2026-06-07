# Create a calculator capable of performing addition, subtraction, multiplication and division
# operations on two numbers. Your program should format the output in a readable manner!
print("\n")
print("\"Welcome to Gourav's Calculator\"")
print("\n")
a = int(input("Enter the First Number: "))
print("Enter the operation's operator that you have to performe")
print("Enter + for addition")
print("Enter - for subtraction")
print("Enter * for multiplixation")
print("Enter / for division")
x = input("Enter operator: ")
if(x == '+'):
    b = int(input("Enter the Second Number: "))
    print("Addition: ",a,"+",b,"=",a+b)
elif(x == '-'):
    b = int(input("Enter the Second Number: "))
    print("Subtraction: ",a,"-",b,"=",a-b)
elif(x == '*'):
    b = int(input("Enter the Second Number: "))
    print("Multiplication: ",a,"*",b,"=",a*b)
elif(x == '/'):
    b = int(input("Enter the Second Number: "))
    print("Division:",a,"/",b,"=",a/b)    
else:
    print("You Entered invalid Operator")
print("\nThank you please come again:)")    



