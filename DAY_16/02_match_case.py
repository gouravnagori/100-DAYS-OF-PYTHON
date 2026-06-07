x = int(input("Enter the number: "))
match x:
    case 0:
        print("x is zero") 
    case 100:
        print("x is 100")
    case _ if x==50:
        print("x is 50")
    case _ if x>100 and x<500:
        print(x,"is between 100 and 500")
    case _:
        print(x,"is greater than 500")    

        
