n = int(input())
cities = map(int, input().split())
m = int(input())
shelters = list(map(int, input().split()))

for i in range(len(shelters)):
    shelters[i] = [i + 1, shelters[i]]

shelters.sort(key=lambda x: x[1])


def find_value(x):
    if x < shelters[0][1]:
        return shelters[0][0]
    if x > shelters[-1][1]:
        return shelters[-1][0]

    l = 0
    r = len(shelters) - 1

    while r - l > 1:
        m = (r + l) >> 1
        if shelters[m][1] < x:
            l = m
        else:
            r = m

    if x - shelters[l][1] < shelters[r][1] - x:
        return shelters[l][0]
    else:
        return shelters[r][0]


resList = [find_value(v) for v in cities]
print(*resList)
