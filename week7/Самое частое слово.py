d = {}

fileIn = open("input.txt")
words_list = fileIn.read().split()

for word in words_list:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

m = 0
word = ''
for key, value in d.items():
    if value > m:
        m = value
        word = key
    elif value == m:
        if key < word:
            word = key

print(word)
