for i in range(1,38):
    if(i==11):
        break #it exit to entire loop or we can say breaking out of the loop
    print(2*i)



for i in range (1,11):
    if i ==6:
        continue #just skip that iteration only
    print(5*i)    

while True:
    num = int(input('Enter only positive number: '))
    if num < 0:
        break