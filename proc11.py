def minmax(x,y):
    l=x
    g=y
    if y<x:
        x=g
        y=l
    else:
        x=l
        y=g
a=float(input())
b=float(input())
c=float(input())
d=float(input())
minmax(a,b)
minmax(c,d)
minmax(a,c)
minmax(b,d)
print("min",a,'max',d)
