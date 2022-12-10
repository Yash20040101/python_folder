def num(n):
    c=0
    for i in range(2,n//2):
        if(n%i==0):
            c=1
            break
    if(c==1):
        return "nonprime number"
    else:
        return "prime number"
print(num(int(input("enter a number:"))))
