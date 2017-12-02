a = list(map(int, input().split()))
b = list(map(int, input().split()))


def merge(A, B):
    newList = A + B
    for passnum in range(len(newList)-1, 0, -1):
        for i in range(passnum):
            if newList[i] > newList[i + 1]:
                newList[i], newList[i + 1] = newList[i + 1], newList[i]
    return newList

print(*merge(a, b))
