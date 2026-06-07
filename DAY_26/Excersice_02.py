# Create a python program capable of greeting you with
# Good Morning, Good Afternoon and Good Evening. Your
# program should use time module to get the current hour.
# Here is a sample program and documentation link for you:

import time
time = int(time.strftime('%H'))
print(time)
if time>=4 and time<12:
    print("Good Morning")
elif time>=12 and time<16:
    print("Good Afternoon")
elif time>=16 and time<20:
    print("Good Evening")
else:
    print("Good Night")           

    