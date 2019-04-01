def InvertDigits(k):
    t=0
    while k!=0:
        t=t*10+k%10
        k=k//10
    return t
for i in range(0,5):
    k=int(input())
    print(int(InvertDigits(k)))
