def rings(r1,r2):
    s1=3.14*r1**2
    s2=3.14*r2**2
    return abs(s1-s2)
r11=float(input())
r12=float(input())
print(rings(r11,r12))
r21=float(input())
r22=float(input())
print(rings(r21,r22))
r31=float(input())
r32=float(input())
print(rings(r31,r32))