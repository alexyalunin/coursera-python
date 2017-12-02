inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
a = []

for line in inFile:
    s = line.split()
    a.append((s[0], s[1], s[3]))

a.sort()

for i in a:
    print(*i, file=outFile)

inFile.close()
outFile.close()
