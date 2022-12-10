a=int(input("enter a number"))
c=0
while a>0:
    c+=1
    a//10
if(c==3):
    print("three digit number")
else:
    print("not three digit number")
