max = 0
res = 0

n = int(input())

while n != 0:
    if n == max:
        res += 1
    if n > max:
        res = 0
        max = n
    n = int(input())

print(res)
