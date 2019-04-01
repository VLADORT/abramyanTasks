a=int(input())
b=int(input())
n=0
for i in reversed(range(a+1,b)):
    n+=1
    print(i)
print(n)