# Известно, что фамилии всех участников — различны. Сохраните в массивах список всех участников и выведите его, отсортировав по фамилии в лексикографическом порядке. При выводе указываете фамилию, имя участника и его балл.
#
# Используйте для ввода и вывода файлы input.txt и output.txt с указанием кодировки utf8. Например, для чтения откройте файл с помощью open('input.txt', 'r', encoding='utf8')


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
