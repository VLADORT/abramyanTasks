def AddRightDigit(k,d):
    k=k*10+d
    return k
for i in range(0,2):
    k=int(input())
    d=int(input())
    print(AddRightDigit(k,d))