a=int(input())
b=int(input())
c=int(input())
if abs(a-b)>abs(a-c):
    print(c,abs(a-c))
elif abs(a-b)<abs(a-c):
    print(b,abs(a-b))
else:
    print(' расстояние одинаковое:', abs(a-b))