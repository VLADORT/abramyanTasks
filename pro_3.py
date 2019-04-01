def AMean(X, Y):
    return (X + Y) / 2,(X * Y)**1/2
A = float(input())
B = float(input())
C = float(input())
D = float(input())
print(AMean(A,B))
print(AMean(A,C))
print(AMean(A,D))