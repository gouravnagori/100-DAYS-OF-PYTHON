# Generators generate values on the fly

def my_generator():
    for i in range(11):
        # complex computation
        yield i

gen = my_generator()
# print(next(gen))        
# print(next(gen))        
# print(next(gen))        
# print(next(gen))        
# print(next(gen))        
# print(next(gen))        
# print(next(gen))        
# print(next(gen))        
# print(next(gen))        

# Better way
for h in  gen:
    print(h)
