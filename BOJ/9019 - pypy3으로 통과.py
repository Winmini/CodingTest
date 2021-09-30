from collections import deque
import sys

test_case = int(input())
dic = {1: 'D', 2:'S', 3:'L', 4:'R'}
for _ in range(test_case):
    A, B = [i for i in sys.stdin.readline().split()]
    N = [0, 0, 0, 0]
    M = [0, 0, 0, 0]
    dp = [[0] * 2 for _ in range(10000)]
    for idx, i in enumerate(A[::-1]):
        N[-idx - 1] = int(i)
    for idx, i in enumerate(B[::-1]):
        M[-idx - 1] = int(i)
    q = deque([N])
    while True:
        d1, d2, d3, d4 = q.popleft()
        if [d1, d2, d3, d4] == M:
            break
        n = (((10 * d1) + d2) * 10 + d3) * 10 + d4
        D = n * 2 % 10000
        S = (n - 1) % 10000 
        L = (((10 * d2) + d3) * 10 + d4) * 10 + d1
        R = (((10 * d4) + d1) * 10 + d2) * 10 + d3
        cnt = 1
        for i in D, S, L, R:
            if dp[i][1] == 0:
                q.append([i // 1000, (i - (i // 1000)*1000) // 100, (i - (i // 100)*100) // 10, i - (i // 10) * 10])
                dp[i][0] = n
                dp[i][1] = cnt
            cnt += 1
    answer = int(B)
    result = []
    while answer != int(A):
        result.append(dp[answer][1])
        answer = dp[answer][0]
    for i in result[::-1]:
        print(dic[i], end='')
    print()