# Найдите количество положительных элементов в данном списке.

str = input().split()
res = 0

for i in str:
    if int(i) > 0:
        res += 1

print(res)
