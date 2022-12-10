n=int(input("enter number "))
sum=0
c=0
a=0
b=n

while(b>0):
    b=b//10
    sum=sum+1
while n>0:
    a=a+(10**(sum-1))*(n%10)
    n=n//10
    sum-=1
print(a)  
