a=int(input("enter number"))
b=int(input("enter number"))
max1=1
count=0
count1=0
if(a>=b):
    for i in range(2,a//2+1):
        while a%i==0 and b%i==0:
            count1+=1
            a=a/i
            b=b/i
        if(count1>count):
            max1=i
            count=count1
            count1=0
    print(max1)
else:
    for i in range(2,b//2+1):
        while a%i==0 and b%i==0:
            count1+=1
            a=a/i
            b=b/i
        if(count1>count):
            max1=i
            count=count1
            count1=0
    print(max1)
    
    
