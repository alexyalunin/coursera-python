def printReverse(n):
    if n != 0:
        printReverse(int(input()))
        print(n)

a = int(input())

print(printReverse(a))
