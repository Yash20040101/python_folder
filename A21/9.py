def f1(a,n):
    if n==1:
        print(a)
    else:
        
        f1(a,n-1)
        print(a*n)
a=int(input("enter number to find its multiple"))        
n=int(input("enter number"))
f1(a,n)    
