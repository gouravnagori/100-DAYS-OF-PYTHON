# list = [1,2,4,6,7,4,3,5,67,4,3,5,6]
# i = 0
# while(i<len(list)):
#     print(list[i])
#     i+=1

# list = [1,2,4,6,7,4,3,5,67,4,3,5,6]
# for i in list:
#     print(i)

# tup = (12,43,2,34,5,23,2,4,3)
# for i in tup:
#     print(i)

# num = int(input("Enter a number: "))
# for i in range(2,num):
#     if num%i == 0:
#         print("Number is not prime")
#         break
# else:
#     print("Number is prime")    
    
# num = 0 
# num = int(input("Enter the number: "))
# for i in range(num):
#     num = num+i
    
# print(num)


'''
for n = 3
print this pattern
  *
 ***
*****

'''

# n = int(input("Enter a number: "))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     print("*"*(2*i - 1),end="")
#     print("")


'''
*
**
***
****
 '''
# n = int(input('Enter a number: '))
# for i in range(1,n+1):
#     print("*"*i)

'''
* * * * * *
*         *
*         *
*         * 
*         *
* * * * * *

# '''
# n = int(input(">>>"))
# for i in range (1,n+1):
#     if i == 1 or i == n:
#         print(' *'*n,end="")
#     else:
#         print(" *",end="")
#         print("  "*(n-2),end="")
#         print(" *",end="")
#     print("")    


'''
 write a program to print multiplication table of n in reverse oreder

'''
n = int(input("Enter a number: "))
for i in range(10,0,-1):
    print(f"{n}x{i}=",n*i)