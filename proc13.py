def sortdec3(a,b,c):
    if a < c:
        t = c
        c = a
        a = t
    elif b<c:
        t = c
        c = b
        b = t
    elif a<b:
        t=b
        b=a
        a=t
    print(a,b,c)
a1=float(input())
b1=float(input())
c1=float(input())
sortdec3(a1,b1,c1)
a2=float(input())
b2=float(input())
c2=float(input())
sortdec3(a2,b2,c2)


