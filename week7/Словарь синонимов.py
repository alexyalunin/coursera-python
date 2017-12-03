n = int(input())
p = dict()

for j in range(n):
    a = input().split()
    p[a[0]] = a[1]
    p[a[1]] = a[0]

print(p[input()])
