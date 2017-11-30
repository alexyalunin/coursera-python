p = int(input())
x = int(input())
y = int(input())

res = x * 100 + y
per = res + (res * p / 100)
r = int(per // 100)
k = int(per % 100)

print(r, k)
