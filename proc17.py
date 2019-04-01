def rootcount(a,b,c):
    d=b**2-4*a*c
    if d>0:
        return 2
    elif d==0:
        return 1
    elif d<0:
        return 0
a1=float(input())
b1=float(input())
c1=float(input())
print(rootcount(a1,b1,c1))
a2=float(input())
b2=float(input())
c2=float(input())
print(rootcount(a2,b2,c2))
a3=float(input())
b3=float(input())
c3=float(input())
print(rootcount(a3,b3,c3))


