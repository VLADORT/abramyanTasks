def AddLeftDigit(d,k):
    t=10
    while k>t:
        t*=10
        k+=d*t
    return k
for i in range(0,2):
    k=int(input())
    print(AddLeftDigit(d,k))
