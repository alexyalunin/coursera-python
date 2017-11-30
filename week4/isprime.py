def isPrime(n):
    i = 2
    while i <= n ** (1 / 2):
        if n % i == 0:
            return 'NO'
        else:
            i += 1
    return 'YES'

print(isPrime(int(input())))