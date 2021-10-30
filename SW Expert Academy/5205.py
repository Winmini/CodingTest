def quickSort(A, l, r):
    if l < r:
        s = partition(A, l, r)
        quickSort(A, l, s-1)
        quickSort(A, s+1, r)


def partition(A, l, r):
    p = A[l]
    i = l + 1
    j = r
    while i <= j:
        while(i <= j and A[i] <= p): i += 1
        while(i <= j and A[j] >= p): j -= 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j


T = int(input())
for test_case in range(1, T+1):
    answer = 0
    N = int(input())
    ai = [int(i) for i in input().split()]
    quickSort(ai, 0, len(ai)-1)
    print('#' + str(test_case) + ' ' + str(ai[len(ai)//2]))