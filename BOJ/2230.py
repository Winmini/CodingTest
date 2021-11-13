import sys


N, M = [int(i) for i in sys.stdin.readline().split()]
array = []
for _ in range(N):
    array.append(int(input()))
array.sort()
ed = 0
answer = int(1e12)
for st in range(N):
    while ed < N and array[ed] - array[st] < M:
        ed += 1
    if ed == N:
        break
    answer = min(answer, array[ed] - array[st])
print(answer)