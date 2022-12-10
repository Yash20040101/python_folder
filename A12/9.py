a=int(input("enter number"))
b=int(input("enter number"))
if(a>b):
    if(a%b==0):
        print("lcm is",a)
    else:
        for i in range(a,a*b+1):
            if(i%a==0 and i%b==0):
                print("lcm is",i)
                break
else:
    if(b%a==0):
        print("lcm is",a)
    else:
        for i in range(b,a*b+1):
            if(i%a==0 and i%b==0):
                print("lcm is",i)
                break
