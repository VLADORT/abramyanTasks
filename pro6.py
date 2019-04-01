def  DigitCountSum(a):
    c=int(0)
    s=int(0)
    while a!=0:
        s+=a%10
        c+=1
        a//=10
    return c,s
for i in range(0,5):
    a=int(input())
    print(DigitCountSum(a))
