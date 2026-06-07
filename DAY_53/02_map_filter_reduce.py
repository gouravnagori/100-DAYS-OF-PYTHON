
#MAP
def sqr(x):
    return x*x

l = [2,5,66,2,8,5,9]

# newl=[]
# for i in l:
#     newl.append(sqr(i))
newl = list(map(sqr,l))

print(newl)


print('\n')
numbers = [1,2,3,4,5,6,7,8,9,10]

double = map(lambda x: x*2 , numbers)
print(list(double))



# FILTER
print('\n')
newnewl = filter(lambda x: x>5,l)
print(tuple(newnewl))


# REDUCE
print('\n')
from functools import reduce
list5 = [1,2,3,4,5]
# [2,3,4,5]
# [6,4,5]
# [24,5]
# [120]
# return 120
fac_of_5 = reduce(lambda x,y: x*y, list5)
print(fac_of_5)


