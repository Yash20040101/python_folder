b=int(input("enter number"))
c=int(input("enter number"))
print("enter 1 for add \n enter 2 for subtract \n enter 3 for multiply \n enter 4 for divide")
a=int(input("enter choice"))
match a:
    case 1:
        d=c+b
        print(d)
    case 2:
        d=b-c
        print(d)
    case 3:
        d=c*b
        print(d)
    case 4:
        d=b/c
        print(d)
    case _:
        print("invalid choice")
              
        
