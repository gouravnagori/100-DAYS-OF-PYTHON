x = {1,2,4,6,'ok'}
y = {2,'ok',5,6,13,234,'hello'}
print(x,y)
print(x.union(y))
print(x.intersection(y))

print("\n")
x.update(y)
print(x)


print("\n")
x1 = {2,2,4,6,5,3,2}
y1 = {2,4,6,0,1}
print(x1,y1)
x1.intersection_update(y1)
print(x1)


print("\n")
x1 = {2,2,4,6,5,3,2}
y1 = {2,4,6,0,1}
print(x1,y1)
print(x1.symmetric_difference(y1))


print("\n")
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)

print("\n")
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities.difference_update(cities2)
print(cities)

