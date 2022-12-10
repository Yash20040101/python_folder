a=int(input("enter a number"))
if(a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12):
    print("number of days is ",31)
elif(a==4 or a==6 or a==9 or a==11):
    print("number of days is",30)
else:
    print("number of days is",28)
