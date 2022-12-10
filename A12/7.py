a=int(input("enter number"))
b=int(input("enter number"))
if(a==b):
    print("they are not co prime")
else:
    if(a>b):
        for i in range(2,b+1):
            if(b%i==0 and a%i==0):
                print("numbers are not co prime")
                break
        else:
            print("numbers are co prime")
    else:
        for i in range(2,a+1):
            if(b%i==0 and a%i==0):
                print("numbers are not co prime")
                break
        else:
            print("numbers are co prime")
                
                
