a=[]
for i in range(25):
    a.append(7)
c=open('bot.txt','w')
for x in a:
    c.write(str(x))
c.close()
c=open('bot.txt')
for h in a:
    while len(a)<50:
        a.append(0)
c=open('bot.txt','w')
for x in reversed(a):
    c.write(str(x)+'\n')
c.close()