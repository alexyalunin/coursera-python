d = {}

fileIn = open("input.txt")
words_list = fileIn.read().split()

for word in words_list:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

for i in sorted(d.items(), key=lambda x: (-x[1], x[0])):
    print(i[0])
