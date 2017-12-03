l1 = list(map(int, input().split()))
d = {}

for el in l1:
    if el in d:
        print("YES")
    else:
        d[el] = 1
        print("NO")
