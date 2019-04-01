def TrianglePS(a):
    p=3*a
    s=a**2*3/4
    return p,s
for i in range(0,3):
    a=float(input())
    print(TrianglePS(a))