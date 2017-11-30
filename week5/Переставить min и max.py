# В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.

a = list(map(int, input().split()))
minIndex = a.index(min(a))
maxIndex = a.index(max(a))
a[minIndex], a[maxIndex] = a[maxIndex], a[minIndex]

print(*a, sep=' ')
