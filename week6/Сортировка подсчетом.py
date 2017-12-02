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
