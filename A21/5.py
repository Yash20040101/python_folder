def f1(n):
    if n==1:
        print(2*n)
    else:
        
        f1(n-1)
        print(2*n)
        
n=int(input("enter number"))
f1(n)    
