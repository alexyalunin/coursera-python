s = input()

index = s.find(' ')

print(s[index + 1:] + " " + s[:index])
