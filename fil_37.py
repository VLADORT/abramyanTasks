q = open('integer.txt', 'w')
q.write("1\n2\n3\n4\n5\n6\n7\n")
q.close()
q = open('integer.txt')
c=[]
for line in q:
    c.append(line)
q.close()
q = open('integer.txt','a')
for l in c[::-1]:
    q.write(l)
q.close()