n=int(input())
k=int(input())
t=n
s=-1
while t>=0:
    t-=k
    s+=1
print(s,t+k)