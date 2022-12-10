a=int(input("enter number"))
b=a+1
while b:
    c=0
    for i in range(2,b//2+1):
        if(b%i==0):
            c=1
            break
    if(c==0):
        print(b)
        break
    
    b=b+1
    
