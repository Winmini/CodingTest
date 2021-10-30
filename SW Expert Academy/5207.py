T = int(input())
for test_case in range(1, T+1):
    answer = 0
    N, M = [int(i) for i in input().split()]
    A = sorted([int(i) for i in input().split()])
    B = [int(i) for i in input().split()]
    for i in B:
        start = 0
        end = len(A) - 1
        cnt = 0
        x = 0
        while start <= end:
            middle = (start + end) // 2
            if A[middle] == i:
                answer += 1
                break
            if A[middle] < i:
                start = middle + 1
                if x == 1:
                    break
                x = 1
            else:
                end = middle - 1
                if x == 2:
                    break
                x = 2
    print('#' + str(test_case) + ' ' + str(answer))