a=int(input())
str=''
if a==0:
    str+='нульове число'
if a>0:
    str+='додатнє '
elif a<0:
    str+='від*ємне '
if a%2==0 and a!=0:
    str+='парне число'
elif a%2==1:
    str+='непарне число'
print(str)


