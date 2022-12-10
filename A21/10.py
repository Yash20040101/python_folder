def f1(n):
    
    if(n>0):
        print(n%10,end='')
        f1(n//10)
        
        
n=int(input("enter number"))
f1(n)    
