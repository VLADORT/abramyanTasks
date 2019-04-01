def AMean(X, Y):
    return (X + Y) / 2
def GMean(X, Y):
    return (X * Y)**1/2
A = float(input())
B = float(input())
C = float(input())
D = float(input())
print(AMean(A, B), ' ', GMean(A, B))

print(AMean(A, C), ' ', GMean(A, C))

print(AMean(A, D), ' ', GMean(A, D))