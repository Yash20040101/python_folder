def f1(n):
    if n==1:
        print(n)
    else:
        
        f1(n-1)
        print(n**3)
        
n=int(input("enter number"))
f1(n)    
