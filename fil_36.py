q = open('integer.txt', 'w')
q.write("1\n2\n3\n4\n5\n6\n7")
q.close()
q = open('integer.txt')
c= open('integ.txt', 'w')
for line in q:
    c.write(line)
c.close()
q.close()
c = open('integ.txt')
q = open('integer.txt','a')
q.write('\n')
for l in c:
    q.write(l)
c.close()
q.close()