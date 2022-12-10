a=input("enter string1")
b=input("enter string2")
match a==b:
    case True:
        print("identical string")
    case False:
        if a>b:
            print("string2 comes before string 1")
        else:
            print("string1 comes before string 2")
