# Write a program to clear the clutter inside a folder on your computer.
# You should use os module to rename all the png images from 1.png all
# the way till n.png where n is the number of png files in that folder. Do
# the same for other file formats

# import os
# os.mkdir("DAY_68/data")

import os
i = 1
files = os.listdir("DAY_68/data")
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"DAY_68/data/{file}",f"DAY_68/data/{i}.png")    
        i += 1