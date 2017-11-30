def fastPow(a, n):
    if n != 0:
        if n % 2 == 0:
            return fastPow(a ** 2, n / 2)
        elif n % 2 == 1:
            return a * fastPow(a, n - 1)
    return 1

a = float(input())
n = int(input())

print(fastPow(a, n))
