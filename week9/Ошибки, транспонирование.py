# Добавьте в программу из предыдущей задачи класс MatrixError, содержащий внутри self поля matrix1 и matrix2 (ссылки на матрицы).
#
# В класс Matrix внесите следующие изменения:
#
# Добавьте в метод __add__ проверку на ошибки в размере входных данных, чтобы при попытке сложить матрицы разных размеров было выброшено исключение MatrixError таким образом, чтобы matrix1 поле MatrixError стало первым аргументом __add__ (просто self), а matrix2 — вторым (второй операнд для сложения).
# Реализуйте метод transpose, транспонирующий матрицу и возвращающую результат (данный метод модифицирует экземпляр класса Matrix)
# Реализуйте статический метод transposed, принимающий Matrix и возвращающий транспонированную матрицу. Пример статического метода.

from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    def __init__(self, list):
        self.list = deepcopy(list)

    def __str__(self):
        rows = []
        for row in self.list:
            rows.append('\t'.join(map(str, row)))
        return '\n'.join(rows)

    def __add__(self, mtr):
        if self.size() == mtr.size():
            rows = deepcopy(self.list)
            for row in range(len(self.list)):
                for i in range(len(self.list[row])):
                    rows[row][i] += mtr.list[row][i]
        else:
            raise MatrixError(self, mtr)
        return Matrix(rows)

    def __mul__(self, n):
        rows = deepcopy(self.list)
        for row in range(len(self.list)):
            for i in range(len(self.list[row])):
                rows[row][i] *= n
        return Matrix(rows)

    @staticmethod
    def transposed(m):
        return Matrix(list(map(list, zip(*m.list))))

    def transpose(self):
        newList = list(map(list, zip(*self.list)))
        self.list = newList
        return self

    def size(self):
        return len(self.list), len(self.list[0])

    __rmul__ = __mul__


exec(stdin.read())
