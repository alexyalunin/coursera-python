n = int(input())
if 11 <= n <= 14:
    print(n, 'korov')
else:
    k = n % 10
    if k == 0 or (5 <= k <= 9):
        print(n, 'korov')
    if k == 1:
        print(n, 'korova')
    if 2 <= k <= 4:
        print(n, 'korovy')
