a=int(input("enter number"))
b=int(input("enter number"))
c=0
for i in range(a,b+1):
    for j in range(2,i//2+1):
        if(i%j==0):
            c=1
            break
    if(c==0):
        print(i)
    c=0
