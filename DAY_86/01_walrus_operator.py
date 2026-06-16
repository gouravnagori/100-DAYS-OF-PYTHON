# The walrus operator in python
# Walrus operator allows you to assign values within an expression.
# this can be useful when you need to use a value multiple time in a loop,
# but don't want to repate the calculation.
# this is newwly add feature
print(a := True)

number = [1,3,4,66,3,6,3]

while (n:= len(number)) > 0:
    print(number.pop())



# # aam jindgi
# foods = list()
# while True:
#     food = input("Enter the food you want: ")
#     if food == 'quit':
#         break
#     foods.append(food)    
# print(foods)    

# mentos jindgi with walrus operator
foods = list()
while (food := input("enter the food you want: ")) != 'quit':
    foods.append(food)
print(foods)

