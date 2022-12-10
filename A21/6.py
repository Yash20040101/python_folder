def f1(n):
    if n==1:
        print(2*n)
    else:
        print(2*n)
        f1(n-1)
        
        
n=int(input("enter number"))
f1(n)    
