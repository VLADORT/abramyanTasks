def PowerA234(a):
    b=a**2
    c=a**3
    d=a**4
    return  b,c,d
for i in range(0,5):
    a=float(input())
    print(PowerA234(a))