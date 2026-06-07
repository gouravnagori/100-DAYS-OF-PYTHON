# Coding:
#   if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# # Decoding:
# # if the word contains less than 3 characters, reverse it
# # else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to
# the beginning
# 
# Your program should ask whether you want to code or decode

coding = input('\nEnter 1 for coding and 0 for decoding: ')

str = input("enter message: ")

if(coding):
    if(len(str)>=3):
        str = str[1:]+str[0]
        print(f"skd{str}jdk")
    else:
        print(str[::-1])
else:
    if(len(str)<=2):
        print(str[::-1])
    else:
        str = str[-4]+str[3:-4]
        print(str)       
   
   
    # skdayshreejjdk