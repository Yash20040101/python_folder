a=input("enter string")
a=a.strip()
print(a)
match a:
    case a if ' ' in a:
        print("multi word string")
    case _:
        print("single word string")
