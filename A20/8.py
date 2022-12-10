def f1(a):
    c1=c2=0
    for i in a:
        if i.islower():
            c1+=1
        else:
            c2+=1
    print(c1,c2)
a=input("string")
f1(a)
