l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

print(*sorted(list(set(l1) & set(l2))))
