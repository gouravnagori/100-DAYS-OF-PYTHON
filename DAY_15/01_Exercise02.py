# Excersice 2: Good Morning Sir

# Create a python program capable of greeting you with Good Morning,
# Good Afternoon and Good Evening. Your program should use time module
# to get the current hour. Here is a sample program and documentation link
# for you:


# import time
# timestamp = time.strftime( '%H:%M:%S')  #formate = 17:04:54
# print(timestamp)
# timestamp = time.strftime( '%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime( '%S')
# print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime



#                        ANSWER
import time
currenttime = time.strftime('%H:%M:%S')
print("Current Time is",currenttime)
hour = int(time.strftime('%H'))
print("current Hour: ",hour)


if hour>=4 and hour < 12:
    print("Good Morning")
elif hour>=12 and hour < 19:
    print("Good Evening")    
else:
    print("Good Night")    


