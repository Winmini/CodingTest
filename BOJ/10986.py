from collections import Counter
import sys

N, M = [int(i) for i in sys.stdin.readline().split()]
A = [int(i) for i in sys.stdin.readline().split()]
pSum = [0] * (N+1)

for i in range(N):
    pSum[i+1] = pSum[i] + A[i]

count = Counter([i % M for i in pSum])
cnt = 0
for i in count:
    if count[i] >= 2:
        cnt += count[i] * (count[i] -1) // 2
print(cnt)