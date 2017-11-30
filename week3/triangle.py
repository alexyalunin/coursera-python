a = float(input())
b = float(input())
c = float(input())

p = (a + b + c) / 2.0

print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
