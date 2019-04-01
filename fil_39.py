q = open('integer.txt', 'w')
q.write("1\n2\n4\n3\n5\n6\n10")
q.close()
q=open('integer.txt')
a=[]
for line in q:
    line=int(line)
    a.append(line)
q = open('integer.txt', 'w')
for g in a:
    if g in range(5,11):
        q.write(str(g)+'\n')
    q.write(str(g)+'\n')
q.close()

