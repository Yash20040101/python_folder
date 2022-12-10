a=int(input("enter number"))
b=0
c=1
if(a==1):
    print(b)
elif(a==2):
    print(b,c)
else:
    print(b)
    print(c)
    for i in range(a-2):
        d=b+c
        print(d)
        b=c
        c=d
