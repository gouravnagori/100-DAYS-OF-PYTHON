def calculateavg(a,b,c):
    avg = (a+b+c)/3
    print(avg)

def greater(a,b):
    if a>=b:
        print(a,"is greater or equal")
    else:
        print(b,"is greater")

def multiplication(a,b):
    pass #with the help of pass we can declear function later       

calculateavg(1,2,3)
greater(37,46)


def info(fname,mname):
    print(fname,"is your father and",mname,"is your mother")

fname = input("Enter your father's name: ")
mname = input("Enter your mother's name: ")
info(fname,mname)

