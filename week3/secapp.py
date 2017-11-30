str = input()

f1 = str.find('f')
f2 = str.find('f', f1 + 1)

if f1 == -1:
    print(-2)
elif f2 == -1:
    print(-1)
else:
    print(f2)
