import sys

N, M = [int(i) for i in sys.stdin.readline().split()]
gun = [int(i) for i in sys.stdin.readline().split()]
pSub = [0] * (N-1)
pSum = [0] * N
for i in range(N-1):
    pSub[i] = abs(gun[i+1] - gun[i])

for i in range(N-1):
    pSum[i+1] = pSum[i] + pSub[i]

for _ in range(M):
    i, j = [int(i) for i in sys.stdin.readline().split()]
    print(pSum[j-1] - pSum[i-1])