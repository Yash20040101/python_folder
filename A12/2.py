n=int(input("enter number "))
c1=0
for i in range(2,n//2+1):
    if(n%2==0):
        c1=1
        break
if(c1==1):
    print("not prime")
else:
    print("prime number")
