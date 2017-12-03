biggest = int(input())
res = set(range(1, biggest + 1))
a = input()

while a != "HELP":
    a = set(map(int, a.split()))
    if input() == "YES":
        res &= a
    else:
        res -= a
    a = input()

print(*sorted(res))
