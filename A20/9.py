def f1(a):
     l=list(a)
     l=sorted(l)
     b=97
     c=0
     while b<=122:
         if(chr(b) not in l):
             c=1
             break
         b+=1
         
     if(c==1):
        print("not panagram")
     else:
        print("panagram")
f1(input("enter string"))
            
             
             
