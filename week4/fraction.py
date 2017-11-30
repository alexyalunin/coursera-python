import math


def ReduceFraction(n, m):
    a = math.gcd(n, m)
    return (n // a, m // a)

a = int(input())
b = int(input())

(a, b) = ReduceFraction(a, b)

print(a, b)
