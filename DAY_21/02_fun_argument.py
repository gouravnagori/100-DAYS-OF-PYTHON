def average(a,v):
    print("The average is", (a+v)/2)

average(3,6)


     #DEFAULT ARGUMENT
print("\nDEFALUT ARGUMENT")
def sum(a=3 , b=35):
    print("sum is:",a+b)

sum()    
sum(23,31) #now the output is 54

sum(35)
sum(b=5)


      #KEYWORD ARGUMENT
print("\nKEYWORD ARGUMENT")
def sub(a,b):
    print("the sub is:",a-b)

sub(b=34,a=2)    
sub(a=3,b=2)


    #REQUIRED ARGEMENT
print("\nREQUIRED ARGUMENT")
def mul(a,b,c=4):
    print("The mul is",a*b*c)

mul(a=5,b=3)
mul(a=22,b=2)



      #VARIABLE-LENGHT ARGUMENT
print("VARIABLE-LENGTH ARGUMENT")
def avg(*nums):
    print(type(nums))
    sum = 0
    for i in nums:
        sum = sum+i
    # print("Avg is",sum/len(nums))
    return sum/len(nums) 

c = avg(3,4,2,4,40,4,3,36,22)
print(c)


def name(**name):
     print(type(name)) 
     print("Hello,", name["fname"], name["mname"],name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname ="James")