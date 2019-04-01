q = open('integer.txt', 'w')
q.write("-11\n2\n4\n3\n5\n6")
q.close()
q=open('integer.txt')
a=[]
for line in q:
    line=int(line)
    if line>=0:
        a.append(line)
q = open('integer.txt', 'w')
for g in a:
    q.write(str(g)+'\n')
q.close()
