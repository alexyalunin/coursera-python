fin = open("input.txt")
words_list = fin.read().split()

print(len(set(words_list)))
