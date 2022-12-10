a=int(input("enter length of sides of triangle"))
b=int(input("enter length of sides of triangle"))
c=int(input("enter length of sides of triangle"))
print("enter 1 to check lengths are of isosceles triangle \n enter 2 to check lengths are of right triangle \n enter 3 to check lengths are of equilateral triangle \n enter 4 to exit")
d=int (input("enter your choice"))
if a+b>c and b+c>a and c+a>b:
    match d:
        case 1:
            if (not(a==b==c)) and a==b or b==c or a==c:
                print("sides are of isosceles triangle")
            else:
                print("not isosceles triangle")
        case 2:
            if (a*a+b*b)==c*c or (c*c+b*b)==a*a or (a*a+c*c)==b*b:
                print("sides are ofright angled triangle")
            else:
                print("sides are not of right angled triangle")
        case 3:
            if a==b==c:
                print("sides are of equilateral triangle")
            else:
                print("sides are not of equilateral triangle")
        case 4:
            print("exit")
else:
    print("invalid sides")
