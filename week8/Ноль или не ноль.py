# Проверьте, есть ли среди данных N чисел нули.
#
# Формат ввода
#
# Вводится число N, а затем N чисел.
#
# Формат вывода
#
# Выведите True, если среди введенных чисел есть хотя бы один нуль, или False в противном случае.

from itertools import repeat
print(0 in list(map(lambda r: int(r()), repeat(input, int(input())))))
