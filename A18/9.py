a=dict(a=20,b=10,c=34)
b=dict(d=34,e=45,f=75)
c={}
for i in a:
    c[i]=a[i]
for i in b:
    c[i]=b[i]
print(c)
