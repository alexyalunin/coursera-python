def sum(a, b):
    if b >= 1:
        a += 1
        b -= 1
        return sum(a, b)
    return a

print(sum(int(input(), int(input()))))
