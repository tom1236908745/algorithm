x,y,z=map(int,input().split())

if z % 2 == 0:
    x = x ** 2
    y = y ** 2

if x > y:
    print(">")
elif x < y:
    print("<")
else:
    print("=")


