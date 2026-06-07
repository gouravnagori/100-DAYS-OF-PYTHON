# Python - else in Loop

# As you have learned before, the else clause is used along with
# the if statement.

# Python allows the else keyword to be used with the for and
# while loops too. The else block appears after the body of the
# loop. The statements in the else block will be executed after all
# iterations are completed. The program exits the loop only after
# the else block is executed.

# Syntax

# for counter in sequence:
# #Statements inside for loop block
# else:
# #Statements inside else block

for i in range(6):
    print(i)
else:
    print('end of the loop')   


print('\n')
for i in ():
    print(i)
else:
    print("end of the loop")


print('\n')
for i in range(7):
    print(i)
    if i == 5:
        break
else:
    print('end of the loop')


print('\n')
i == 0
while i < 7:
    print(i)
    i = i+1
    if i == 5:
        break
else:
    print('end of the loop')        