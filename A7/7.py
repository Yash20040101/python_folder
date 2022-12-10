a=int(input("enter a number"))
match a:
    case 0:
        print("zero number")
    case _:
        if(a>0):
            print("positive number")
        else:
            print("negative number")
