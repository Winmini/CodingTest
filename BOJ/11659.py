import sys

N, M = [int(i) for i in sys.stdin.readline().split()]
num = [int(i) for i in sys.stdin.readline().split()]
pSum = [0] * (N+1)
for i in range(N):
    pSum[i+1] = pSum[i] + num[i]
    
for _ in range(M):
    s, e = [int(i) for i in sys.stdin.readline().split()]
    print(pSum[e] - pSum[s-1])