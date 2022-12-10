a=input("enter colour")
b=None
if 'red' in a:
    b='red'
elif 'blue' in a:
    b='blue'
elif 'orange' in a:
    b='orange'
elif 'white' in a:
    b='white'
elif 'black' in a:
    b='black'
elif 'yellow' in a:
    b='yellow'
match b:
    case 'yellow':
        print("monday")
    case 'blue':
        print("tuesday")
    case 'orange':
        print("wednesday")
    case 'white':
        print("thursday")
    case 'black':
        print("friday")
    case 'red':
        print("saturday")
    case _:
        print("sunday")
    
