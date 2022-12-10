i=2

while i<100:
    c1=0
    for j in range(2,i//2+1):
        if(i%j==0):
            c1=c1+1
            break
    if(c1==0):
        print(i)
    i+=1
