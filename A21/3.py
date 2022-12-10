def f1(n):
    if n==1:
        print(n)
    else:
        
        f1(n-1)
        print(2*n-1)
        
n=int(input("enter number"))
f1(n)    
