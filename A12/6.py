a=int(input("enter number"))
b=2
c=0
d=0
while a:
    for j in range(2,b//2+1):
        if(b%j==0):
            c=1
            break
    if(c==0):
        print(b)
        d+=1
        if(d==a):
            break
           
    b=b+1
    c=0
    
    
