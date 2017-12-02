a = list(map(int, input().split()))
b = list(map(int, input().split()))


def merge(A, B):
    cl = []
    i, j = 0, 0
    for k in range(len(A) + len(B)):
        if i < len(A) and j < len(B):
            if A[i] < B[j]:
                cl.append(A[i])
                i += 1
            else:
                cl.append(B[j])
                j += 1
        elif i < len(A):
            cl.append(A[i])
            i += 1
        elif j < len(B):
            cl.append(B[j])
            j += 1
    return cl


print(*merge(a, b))
