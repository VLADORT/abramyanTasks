a=[]
for i in range(56):
    a.append(7)
c=open('bot.txt','w')
for x in a:
    c.write(str(x))
c.close()
c=open('bot.txt')
for h in reversed(a):
    while len(a)>56/2:
        a.remove(h)
c=open('bot.txt','w')
for x in a:
    c.write(str(x)+'\n')
c.close()