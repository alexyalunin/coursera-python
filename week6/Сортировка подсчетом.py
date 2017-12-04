# Дан список из N (N≤2*10⁵) элементов, которые принимают целые значения от 0 до 100.
#
# Отсортируйте этот список в порядке неубывания элементов. Выведите полученный список.
#
# Решение оформите в виде функции CountSort(A), которая модифицирует передаваемый ей список. Использовать встроенные функции сортировки нельзя.

marks = map(int, input().split())


def CountSort(A):
    cntMarks = [0] * 101
    for mark in A:
        cntMarks[mark] += 1
    st = ''
    for nowMark in range(101):
        st += str((str(nowMark) + ' ') * cntMarks[nowMark])
    return st

print(CountSort(marks))
