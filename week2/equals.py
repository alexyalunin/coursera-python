a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if (a <= d | b <= d | c <= d) & (a <= e | a <= e | c <= e):
    print('YES')
else:
    print('NO')
