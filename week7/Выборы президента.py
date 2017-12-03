fileIn = open('input.txt', 'r', encoding='utf8')
fileOut = open('output.txt', 'w', encoding='utf8')

d = {}
n = 0

for line in fileIn:
    candidateName = line.strip()
    d[candidateName] = d.get(candidateName, 0) + 1
    n += 1

l = []

for name, v in d.items():
    l += [(name, v)]
l.sort(key=lambda k: (-k[1], k[0]))

if l[0][1] * 2 > n:
    print(l[0][0], file=fileOut)
else:
    print('\n'.join((l[0][0], l[1][0])), file=fileOut)

fileIn.close()
fileOut.close()
