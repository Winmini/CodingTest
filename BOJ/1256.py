from math import factorial
import sys


N, M, K = [int(i) for i in sys.stdin.readline().split()]
t_len = N+M
x = ['a'] * N + ['z'] * M
size = factorial(N + M) // factorial(N) // factorial(M)
if size < K:
    print(-1)
else:
    answer = ''
    start, end = 0, size
    while True:
        if ((end - start) * N) // (N + M) + start > K:
            answer += 'a'
            end = ((end - start) * N) // (N + M) + start
            N -= 1
        elif ((end - start) * N) // (N + M) + start < K:
            answer += 'z'
            start = ((end - start) * N) // (N + M) + start
            M -= 1
        else:
            answer += 'a'
            N -= 1
            break
    print(answer + M*'z' + N*'a')