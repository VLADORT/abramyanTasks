def sign(x):
    if x<0:
        return -1
    elif x==0:
        return 0
    elif x>0:
        return 1
x1=float(input())
x2=float(input())
print(sign(x1)+sign(x2))