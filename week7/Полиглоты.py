n = int(input())
ld = dict()

for i in range(0, n):
    sb_index = int(input())
    for j in range(0, sb_index):
        l = input()
        if l in ld:
            ld[l] = ld[l] + 1
        else:
            ld[l] = 0

allknow_languages = list()
for l in ld:
    if ld[l] == n - 1:
        allknow_languages.append(l)

print(len(allknow_languages))
for l in allknow_languages:
    print(l)

print(len(ld))
for i in ld:
    print(i)
