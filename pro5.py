def RectPS(x1,x2,y1,y2):
    p=2*(abs(x1-x2)+abs(y1-y2))
    s=abs(x1-x2)*abs(y1-y2)
    return p,s
for i in range(0,3):
    x1=int(input())
    x2=int(input())
    y1=int(input())
    y2=int(input())
    print(RectPS(x1,x2,y1,y2))