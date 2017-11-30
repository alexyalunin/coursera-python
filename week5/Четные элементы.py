# Выведите все четные элементы списка.

str = input().split()

for i in str:
    if int(i) % 2 == 0:
        print(i, end=' ')
