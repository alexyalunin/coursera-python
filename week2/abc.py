a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)
