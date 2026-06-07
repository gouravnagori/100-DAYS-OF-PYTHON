insects = "Ant, bee, butterfly"
print("Slicing")                        
print("lenth of the insects string is",len(insects))
print(insects[0:3]) #including 0 but not including 3
print(insects[0:4])
print(insects[1:12])#including 1 but not including 12
print(insects[0:])
print(insects[:9])


# Negative slicing
print("\nNegative Slicing")
print("yaahoo",insects[-3:-1])
print("yaahoo",insects[len(insects)-3:len(insects)-1])
print(insects[:len(insects)-1])     
print(insects[-3:])
print(insects[-1:-3])#it show space 
# -n = len(string) - n
# -3 => 19 - 3 => 16

nm = "Harry"
print(nm[-4 :- 2])



#
print("\n")
if "our" in "Gourav":
    print("yes")
else:
    print("No")    